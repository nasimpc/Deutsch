"""Build the approved text/audio A1.1 package; never emit a package with missing audio.

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
             '528 cards in source order. Text and German pronunciation; no images.', '',
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
    filenames = sorted({c['audio'] for c in cards})
    missing = [f for f in filenames if not (MEDIA / f).is_file() or (MEDIA / f).stat().st_size < 500]
    if missing:
        raise RuntimeError(f'{len(missing)} audio clips missing. Run the audio command before building.')
    fields = ['ID', 'Headword', 'Details', 'English', 'Audio', 'OriginalGerman',
              'OriginalEnglish', 'SpokenGerman', 'SourceID']
    model = genanki.Model(MODEL_ID, 'German A1.1 — Clean blue text and audio',
                         fields=[{'name': n} for n in fields],
                         templates=[{'name': 'German → English', 'qfmt': FRONT, 'afmt': BACK}],
                         css=(REPO / 'anki/prototype/cards.css').read_text())
    decks = [genanki.Deck(DECK_BASE+n, f'German A1.1::Deck {n:02}') for n in range(1, 19)]
    for card in cards:
        values = [card['card_id'], card['headword'], card['details'], card['english'],
                  audio_button(card['audio']), card['original_german'],
                  card['original_english'], card['speech'], card['source_label']]
        values = [v if i == 4 else html.escape(v) for i, v in enumerate(values)]
        note = genanki.Note(model=model, fields=values,
                            guid=genanki.guid_for('german-a1.1-study', card['card_id']),
                            tags=['A1.1', f'source_{card["source_id"]:03}', f'batch_{card["deck"]:02}'],
                            sort_field=str(card['position']).zfill(3), due=card['position'])
        decks[card['deck']-1].add_note(note)
    package = genanki.Package(decks)
    package.media_files = [str(MEDIA / f) for f in filenames]
    temporary = PACKAGE.with_suffix('.apkg.tmp')
    package.write_to_file(str(temporary))
    temporary.replace(PACKAGE)
    preview()
    print(f'Built {PACKAGE}: 528 cards, 18 subdecks, {len(filenames)} unique MP3 clips.', flush=True)


def preview():
    cards = load_cards()
    assets = {name: 'data:audio/mpeg;base64,' + base64.b64encode((MEDIA / name).read_bytes()).decode()
              for name in {c['audio'] for c in cards} if (MEDIA / name).is_file()}
    template = (REPO / 'anki/a1.1/preview-template.html').read_text()
    data = json.dumps({'cards': cards, 'audio': assets}, ensure_ascii=False).replace('<', '\\u003c')
    page = template.replace('/* DATA */', 'const DATA = ' + data + ';')
    page = page.replace('/* CARD_STYLES */', (REPO / 'anki/prototype/cards.css').read_text())
    (ROOT / 'preview.html').write_text(page)
    print(f'Preview: 528 cards, {len(assets)} available audio clips.', flush=True)


def verify():
    expected = load_cards()
    with zipfile.ZipFile(PACKAGE) as archive, tempfile.TemporaryDirectory() as directory:
        assert archive.testzip() is None
        media = json.loads(archive.read('media'))
        assert set(media.values()) == {c['audio'] for c in expected}
        assert all(name.endswith('.mp3') for name in media.values())
        for number in media:
            assert len(archive.read(number)) >= 500
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
            assert len(model['tmpls']) == 1
            assert model['tmpls'][0]['afmt'] == BACK
            assert not any(s in BACK for s in ['Audio', 'Headword', 'FrontSide', 'img'])
            assert 'autoplay' not in model['tmpls'][0]['qfmt']
            packaged_decks = json.loads(decks)
            for n in range(1, 19):
                assert packaged_decks[str(DECK_BASE+n)]['name'] == f'German A1.1::Deck {n:02}'
            rows = db.execute('select n.flds,c.did,c.due from notes n join cards c on c.nid=n.id order by c.due').fetchall()
            for card, (fields, did, due) in zip(expected, rows):
                values = [html.unescape(v) for v in fields.split('\x1f')]
                assert values[0] == card['card_id']
                assert values[1:4] == [card['headword'], card['details'], card['english']]
                assert values[5:] == [card['original_german'], card['original_english'], card['speech'], card['source_label']]
                assert f'src="{card["audio"]}"' in values[4]
                assert '[sound:' not in fields and 'autoplay' not in fields and '<img' not in fields
                assert did == DECK_BASE+card['deck']
                assert due == card['position']
    report = {'cards': len(expected), 'decks': 18, 'cards_per_deck': [30]*17+[18],
              'unique_audio_clips': len(media), 'images': 0,
              'package_sha256': hashlib.sha256(PACKAGE.read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256((REPO / 'x-flashcards-a1.1.md').read_bytes()).hexdigest(),
              'verified': ['package integrity', 'all source entries and meanings', 'original fields',
                           '528 distinct notes and forward cards', 'source order', 'deck sizes',
                           'all audio bundled', 'English-only answer', 'no images or autoplay']}
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
