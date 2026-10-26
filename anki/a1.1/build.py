"""Build the A1.1 package with approved Deck 01 visuals; never emit a package with missing audio.

Dependencies: genanki, edge-tts. Run prepare, audio, build, then verify.
"""
import argparse
import asyncio
import base64
import hashlib
import html
import json
import re
import shutil
import sqlite3
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
MEDIA = ROOT / 'media'
PACKAGE = ROOT / 'german-a1.1.apkg'
VOICE = 'de-DE-KatjaNeural'
RATE = '-10%'
MODEL_ID = 1792936801
DECK_BASE = 1792936900
IMAGE_MANIFEST = ROOT / 'image-candidates/manifest.json'
FIELDS = ['ID', 'Headword', 'Details', 'English', 'Audio', 'OriginalGerman',
          'OriginalEnglish', 'SpokenGerman', 'SourceID']


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def speech_for(german):
    # Speak lexical alternatives, but not dictionary plurals or grammar labels.
    text = german.replace('(sich)', 'sich')
    text = re.sub(r'\([^)]*\)', '', text).strip()
    if re.match(r'^(der|die|das) ', text):
        text = text.split(',', 1)[0]
    text = text.replace('/', ', ')
    text = re.sub(r'\s*,\s*', ', ', text)
    return text.strip(' -')


def prepare():
    rows = re.findall(r'^- \*\*(\d+[a-z]?)\.\*\* (.+?) — (.+)$',
                      (REPO / 'x-flashcards-a1.1.md').read_text(), re.M)
    provenance = json.loads((REPO / 'anki/vocabulary-levels.json').read_text())
    classified = [c for c in provenance['cards'] if c['level'] == 'A1.1']
    originals = {r['source_id']: r for r in provenance['source_entries']}
    assert len(rows) == len(classified) == 528
    MEDIA.mkdir(exist_ok=True)
    cards = []
    for index, ((label, german, english), record) in enumerate(zip(rows, classified), 1):
        assert (german, english) == (record['german'], record['english'])
        assert int(re.match(r'\d+', label)[0]) == record['source_id']
        speech = speech_for(german)
        key = hashlib.sha256(f'{VOICE}|{RATE}|{speech}'.encode()).hexdigest()[:20]
        headword, details = german, ''
        if re.match(r'^(der|die|das) ', german) and ',' in german:
            headword, details = german.split(',', 1)
            details = details.strip()
        cards.append(dict(position=index, source_label=label, card_id=record['card_id'],
                          source_id=record['source_id'], deck=(index-1)//30+1,
                          german=german, headword=headword, details=details,
                          english=english, speech=speech, audio=f'a11_{key}.mp3',
                          original_german=originals[record['source_id']]['original_german'],
                          original_english=originals[record['source_id']]['original_english']))
    # Reuse only clips with an identical spoken text, voice and speed.
    prototype = REPO / 'anki/prototype'
    audio = json.loads((prototype / 'media-sources.json').read_text())['audio']
    reused = 0
    if audio['voice'] == VOICE and audio['rate'] == RATE:
        cached = {text: prototype / 'media' / f'a1_{i:03}_de.mp3'
                  for i, text in enumerate(audio['spoken_text'], 1)}
        for card in cards:
            target = MEDIA / card['audio']
            source = cached.get(card['speech'])
            if source and source.is_file() and not target.exists():
                shutil.copyfile(source, target)
                reused += 1
    write_json(ROOT / 'cards.json', cards)
    write_json(ROOT / 'audio-manifest.json', {
        'voice': VOICE, 'rate': RATE,
        'clips': {c['audio']: c['speech'] for c in cards},
    })
    lines = ['# German A1.1 — 18 study decks', '',
             '528 cards in source order. Text and German pronunciation; approved visuals in Deck 01 only.', '',
             'Decks 01–17 have 30 cards each; deck 18 has 18.', '']
    for deck in range(1, 19):
        batch = [c for c in cards if c['deck'] == deck]
        lines.extend([f'## Deck {deck:02} — {len(batch)} cards', ''])
        lines.extend(f'- **{c["source_label"]}.** {c["german"]} — {c["english"]}' for c in batch)
        lines.append('')
    (ROOT / 'decks.md').write_text('\n'.join(lines))
    print(f'Prepared {len(cards)} cards; reused {reused} prototype clips.', flush=True)


def load_cards():
    return json.loads((ROOT / 'cards.json').read_text())


def approved_images(cards):
    """Resolve only explicit approvals; keep assignments outside prepare()'s output."""
    if not IMAGE_MANIFEST.exists():
        return {}
    manifest = json.loads(IMAGE_MANIFEST.read_text())
    inventory = {c['card_id']: c for c in cards}
    images = {}
    for card_id, assignment in manifest['assignments_approved'].items():
        card = inventory[card_id]
        assert card['deck'] == 1, f'Images forbidden outside Deck 01: {card_id}'
        record = manifest['cards'][card_id]
        assert (record['german'], record['english']) == (card['german'], card['english'])
        candidate_id = assignment['candidate_id']
        assert record['selected_candidate_id'] == candidate_id
        candidate = next(c for c in record['candidates'] if c['candidate_id'] == candidate_id)
        assert candidate['status'] in ('approved', 'integrated'), candidate_id
        filename = assignment['media_file']
        assert re.fullmatch(r'a11_visual_[A-Za-z0-9_-]+\.(jpg|png|gif|webp)', filename)
        source = (IMAGE_MANIFEST.parent / candidate['local_path']).resolve()
        assert source.is_relative_to(IMAGE_MANIFEST.parent.resolve())
        assert source.is_file(), f'Missing approved image: {source}'
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        assert digest == assignment['sha256'] == candidate['sha256'], f'Changed image: {candidate_id}'
        images[card_id] = dict(filename=filename, source=source, sha256=digest,
                               frames=candidate['frames'], candidate_id=candidate_id)
    # Detect a partially edited approval record instead of silently dropping selections.
    selected = {cid for cid, c in manifest['cards'].items() if c.get('selected_candidate_id')}
    assert set(images) == selected
    assert len({c['filename'] for c in images.values()}) == len(images)
    return images


def answer_field(card, images):
    # Keep all nine field names/ordinals and the note type unchanged on reimport.
    # English text stays exact; the optional image is the only appended answer content.
    answer = html.escape(card['english'])
    if image := images.get(card['card_id']):
        answer += f'<div class="visual"><img src="{image["filename"]}" alt=""></div>'
    return answer


async def synthesize():
    import edge_tts
    clips = json.loads((ROOT / 'audio-manifest.json').read_text())['clips']
    pending = [(filename, text) for filename, text in clips.items()
               if not (MEDIA / filename).exists()]
    gate = asyncio.Semaphore(3)
    completed = 0

    async def one(filename, text):
        nonlocal completed
        async with gate:
            target = MEDIA / filename
            temporary = target.with_suffix('.part')
            for attempt in range(3):
                try:
                    await asyncio.wait_for(
                        edge_tts.Communicate(text, VOICE, rate=RATE).save(str(temporary)),
                        timeout=60)
                    if temporary.stat().st_size < 500:
                        raise ValueError(f'Empty audio for {text}')
                    temporary.replace(target)
                    completed += 1
                    if completed % 10 == 0 or completed == len(pending):
                        print(f'Generated {completed}/{len(pending)} missing clips.', flush=True)
                    return
                except Exception:
                    temporary.unlink(missing_ok=True)
                    if attempt == 2:
                        raise
                    await asyncio.sleep(2 * (attempt+1))
    await asyncio.gather(*(one(filename, text) for filename, text in pending))
    print(f'All {len(clips)} unique pronunciation clips are present.', flush=True)


FRONT = ('<div class="sample-card theme-clean side-front" lang="de">'
         '<div class="word-block"><div class="word">{{Headword}}</div>'
         '{{#Details}}<div class="forms">{{Details}}</div>{{/Details}}</div>'
         '<div class="sound">{{Audio}}</div></div>')
BACK = ('<div class="sample-card theme-clean side-back" lang="en">'
        '<div class="meaning">{{English}}</div></div>')


def audio_button(filename):
    return (f'<audio preload="none" src="{filename}"></audio>'
            '<button type="button" class="pronounce" aria-label="Play German pronunciation" '
            'onclick="var a=this.previousElementSibling;a.pause();a.currentTime=0;'
            'a.play().catch(function(){console.error(\'Pronunciation playback failed\');});">'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9v6h4l5 4V5L7 9H3zm13-4.4v2.1a6 6 0 010 10.6v2.1a8 8 0 000-14.8zm-2 4v6.8a4 4 0 000-6.8z"/></svg></button>')


def build():
    import genanki
    cards = load_cards()
    images = approved_images(cards)
    filenames = sorted({c['audio'] for c in cards})
    missing = [f for f in filenames if not (MEDIA / f).is_file() or (MEDIA / f).stat().st_size < 500]
    if missing:
        raise RuntimeError(f'{len(missing)} audio clips missing. Run the audio command before building.')
    model = genanki.Model(MODEL_ID, 'German A1.1 — Clean blue text and audio',
                         fields=[{'name': n} for n in FIELDS],
                         templates=[{'name': 'German → English', 'qfmt': FRONT, 'afmt': BACK}],
                         css=card_styles())
    decks = [genanki.Deck(DECK_BASE+n, f'German A1.1::Deck {n:02}') for n in range(1, 19)]
    for card in cards:
        values = [card['card_id'], card['headword'], card['details'], card['english'],
                  audio_button(card['audio']), card['original_german'],
                  card['original_english'], card['speech'], card['source_label']]
        values = [v if i == 4 else html.escape(v) for i, v in enumerate(values)]
        values[3] = answer_field(card, images)
        note = genanki.Note(model=model, fields=values,
                            guid=genanki.guid_for('german-a1.1-study', card['card_id']),
                            tags=['A1.1', f'source_{card["source_id"]:03}', f'batch_{card["deck"]:02}'],
                            sort_field=str(card['position']).zfill(3), due=card['position'])
        decks[card['deck']-1].add_note(note)
    package = genanki.Package(decks)
    for image in images.values():
        shutil.copyfile(image['source'], MEDIA / image['filename'])
    package.media_files = [str(MEDIA / f) for f in filenames] + [str(MEDIA / i['filename']) for i in images.values()]
    temporary = PACKAGE.with_suffix('.apkg.tmp')
    package.write_to_file(str(temporary))
    temporary.replace(PACKAGE)
    preview()
    print(f'Built {PACKAGE}: 528 cards, 18 subdecks, {len(filenames)} unique MP3 clips, {len(images)} approved images.', flush=True)


def card_styles():
    return (REPO / 'anki/prototype/cards.css').read_text() + '\n.visual img { max-height: 420px !important; }\n'


def preview():
    cards = load_cards()
    images = approved_images(cards)
    image_assets = {}
    for card_id, image in images.items():
        mime = {'.jpg': 'image/jpeg', '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp'}[image['source'].suffix]
        image_assets[card_id] = 'data:' + mime + ';base64,' + base64.b64encode(image['source'].read_bytes()).decode()
    assets = {name: 'data:audio/mpeg;base64,' + base64.b64encode((MEDIA / name).read_bytes()).decode()
              for name in {c['audio'] for c in cards} if (MEDIA / name).is_file()}
    template = (REPO / 'anki/a1.1/preview-template.html').read_text()
    data = json.dumps({'cards': cards, 'audio': assets, 'images': image_assets}, ensure_ascii=False).replace('<', '\\u003c')
    page = template.replace('/* DATA */', 'const DATA = ' + data + ';')
    page = page.replace('/* CARD_STYLES */', card_styles())
    (ROOT / 'preview.html').write_text(page)
    print(f'Preview: 528 cards, {len(assets)} available audio clips.', flush=True)


def verify():
    import genanki
    expected = load_cards()
    images = approved_images(expected)
    # Compare against source on every verification, not only generated cards.json.
    rows = re.findall(r'^- \*\*(\d+[a-z]?)\.\*\* (.+?) — (.+)$',
                      (REPO / 'x-flashcards-a1.1.md').read_text(), re.M)
    assert [(c['source_label'], c['german'], c['english']) for c in expected] == rows
    assert len(expected) == 528
    with zipfile.ZipFile(PACKAGE) as archive, tempfile.TemporaryDirectory() as directory:
        assert archive.testzip() is None
        media = json.loads(archive.read('media'))
        assert len(media) == len(set(media.values()))
        assert set(media.values()) == {c['audio'] for c in expected} | {i['filename'] for i in images.values()}
        for number in media:
            name = media[number]
            data = archive.read(number)
            assert data == (MEDIA / name).read_bytes(), f'Media bytes differ: {name}'
            if name.endswith('.mp3'):
                assert len(data) >= 500
            else:
                image = next(i for i in images.values() if i['filename'] == name)
                assert hashlib.sha256(data).hexdigest() == image['sha256']
        database = Path(directory) / 'collection.anki2'
        database.write_bytes(archive.read('collection.anki2'))
        with sqlite3.connect(database) as db:
            assert db.execute('pragma integrity_check').fetchone()[0] == 'ok'
            assert db.execute('select count(*) from notes').fetchone()[0] == 528
            assert db.execute('select count(*) from cards').fetchone()[0] == 528
            assert db.execute('select count(distinct guid) from notes').fetchone()[0] == 528
            counts = dict(db.execute('select did,count(*) from cards group by did'))
            assert [counts[DECK_BASE+n] for n in range(1, 19)] == [30]*17+[18]
            models, decks = db.execute('select models,decks from col').fetchone()
            model = json.loads(models)[str(MODEL_ID)]
            assert [f['name'] for f in model['flds']] == FIELDS
            assert model['name'] == 'German A1.1 — Clean blue text and audio'
            assert len(model['tmpls']) == 1
            assert model['tmpls'][0]['qfmt'] == FRONT
            assert model['tmpls'][0]['afmt'] == BACK
            assert not any(s in BACK for s in ['Audio', 'Headword', 'FrontSide', 'img'])
            assert 'autoplay' not in model['tmpls'][0]['qfmt']
            packaged_decks = json.loads(decks)
            for n in range(1, 19):
                assert packaged_decks[str(DECK_BASE+n)]['name'] == f'German A1.1::Deck {n:02}'
            rows = db.execute('select n.flds,c.did,c.due,n.guid,n.mid from notes n join cards c on c.nid=n.id order by c.due').fetchall()
            for card, (fields, did, due, guid, mid) in zip(expected, rows):
                values = [html.unescape(v) for v in fields.split('\x1f')]
                assert values[0] == card['card_id']
                assert values[1:3] == [card['headword'], card['details']]
                assert fields.split('\x1f')[3] == answer_field(card, images)
                assert guid == genanki.guid_for('german-a1.1-study', card['card_id'])
                assert mid == MODEL_ID
                assert values[5:] == [card['original_german'], card['original_english'], card['speech'], card['source_label']]
                assert values[4] == audio_button(card['audio'])
                assert '[sound:' not in fields and 'autoplay' not in fields
                assert '<img' not in ''.join(fields.split('\x1f')[:3] + fields.split('\x1f')[4:])
                if card['deck'] != 1 or card['card_id'] not in images:
                    assert '<img' not in fields
                assert did == DECK_BASE+card['deck']
                assert due == card['position']
            baseline_path = ROOT / 'validation/baseline-content.json'
            if baseline_path.exists():
                baseline = json.loads(baseline_path.read_text())
                assert model['flds'] == baseline['model']['flds']
                assert model['tmpls'] == baseline['model']['tmpls']
                notes = db.execute('select guid,mid,flds,tags from notes order by guid').fetchall()
                assert len(notes) == len(baseline['notes'])
                for old, current in zip(baseline['notes'], notes):
                    assert old[:2] == list(current[:2])
                    assert old[3] == current[3]
                    old_values = old[2].split('\x1f')
                    current_values = current[2].split('\x1f')
                    assert old_values[:3] + old_values[4:] == current_values[:3] + current_values[4:]
                    assert current_values[3].split('<div class="visual">', 1)[0] == old_values[3]
                by_filename = {name: number for number, name in media.items()}
                for name, digest in baseline['media_hashes'].items():
                    assert hashlib.sha256(archive.read(by_filename[name])).hexdigest() == digest
    report = {'cards': len(expected), 'decks': 18, 'cards_per_deck': [30]*17+[18],
              'unique_audio_clips': len({c['audio'] for c in expected}), 'images': len(images),
              'animated_gifs': sum(i['frames'] > 1 for i in images.values()),
              'illustrated_cards': {cid: i['candidate_id'] for cid, i in images.items()},
              'deck_01_image_gaps': 30 - len(images), 'schema_fields': FIELDS,
              'package_sha256': hashlib.sha256(PACKAGE.read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256((REPO / 'x-flashcards-a1.1.md').read_bytes()).hexdigest(),
              'verified': ['package integrity', 'all source entries and meanings', 'original fields',
                           '528 distinct notes and forward cards', 'source order', 'deck sizes',
                           'all audio and approved images bundled byte-for-byte', 'English plus approved image only on backs',
                           'no unapproved images; no images in Decks 02–18', 'no autoplay',
                           'stable GUIDs, model identity and nine-field schema',
                           'baseline vocabulary, fields, tags, templates and audio bytes preserved']}
    write_json(ROOT / 'verification.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'audio', 'build', 'preview', 'verify'])
    command = parser.parse_args().command
    if command == 'audio':
        asyncio.run(synthesize())
    else:
        globals()[command]()
