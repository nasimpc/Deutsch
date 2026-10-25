"""Build the selected blue clean-modern design for the first ten source pairs."""
import base64
import html
import json
import re
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[1] / 'x-flashcards.md'
MEDIA = ROOT / 'media'
THEMES = [('clean', 'Clean blue')]
WORDS = [
    ('ab', '(ab heute)'), ('aber', ''), ('abfahren', '(fuhr ab, abgefahren)'),
    ('die Abfahrt', ''), ('abgeben', '(etw.Akk. Abgeben, gab ab, abgegeben)'),
    ('abholen', '(holte ab, abgeholt)'), ('der Absender', '(die Absenderin)'),
    ('Achtung!', '(die)'), ('die Adresse', 'Adressen'), ('alle', '(alles)'),
]

CSS = r'''
* { box-sizing: border-box; }
.card { margin: 0; padding: 22px; background: #eef4fc; color: #142e58; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.sample-card { width: 100%; max-width: 620px; min-height: 440px; margin: 0 auto; padding: 40px; position: relative; overflow: hidden; text-align: center; }
.word { font-size: clamp(34px, 6vw, 48px); line-height: 1.12; overflow-wrap: anywhere; font-weight: 750; letter-spacing: -1.5px; }
.forms { font-size: 17px; line-height: 1.7; margin-top: 18px; overflow-wrap: anywhere; }
.meaning { font-size: clamp(27px, 4vw, 36px); line-height: 1.3; overflow-wrap: anywhere; }
.sound { margin-top: 32px; }
.sound audio { display: none; }
.pronounce { cursor: pointer; border: 1px solid #b9d2fa; border-radius: 100%; width: 48px; height: 48px; background: #e7f0ff; color: #245edb; display: inline-grid; place-items: center; padding: 0; }
.pronounce svg { width: 23px; height: 23px; fill: currentColor; }
.pronounce:focus-visible { outline: 3px solid #397ef0; outline-offset: 4px; }
.visual { min-width: 0; margin-top: 26px; }
.visual img { display: block; width: auto; max-width: 100% !important; height: auto; max-height: 300px !important; margin: 0 auto; object-fit: contain; }
.theme-clean { background: #fff; border: 1px solid #d6e3fa; border-radius: 28px; color: #16396c; box-shadow: 0 18px 65px #1d4f9912; }
.theme-clean.side-front { display: flex; flex-direction: column; justify-content: center; align-items: center; }
.theme-clean .forms { color: #637b9c; }
.theme-clean .meaning { font-weight: 650; }
.theme-clean .visual { border-radius: 16px; overflow: hidden; background: #f0f5ff; padding: 12px; }
.theme-clean.side-back { display: flex; flex-direction: column; justify-content: center; }
.nightMode .theme-clean, .night_mode .theme-clean { background: #15243d; color: #e2edff; border-color: #334c73; }
.nightMode .theme-clean .forms, .night_mode .theme-clean .forms { color: #aac0e0; }
.nightMode .theme-clean .visual, .night_mode .theme-clean .visual { background: #101d33; }
.nightMode .pronounce, .night_mode .pronounce { background: #203c66; border-color: #416397; color: #b4d2ff; }
@media(max-width: 480px) { .card { padding: 14px; } .sample-card { padding: 28px 22px; min-height: 390px; } }
'''

SPEAKER = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9v6h4l5 4V5L7 9H3zm13-4.4v2.1a6 6 0 010 10.6v2.1a8 8 0 000-14.8zm-2 4v6.8a4 4 0 000-6.8z"/></svg>'


def audio_button(filename):
    # HTML audio is tracked as media but creates no Anki automatic [sound:] event.
    return (f'<audio preload="none" src="{html.escape(filename, quote=True)}"></audio>'
            '<button type="button" class="pronounce" aria-label="Play German pronunciation" '
            'onclick="var a=this.previousElementSibling;a.pause();a.currentTime=0;'
            'a.play().catch(function(){console.error(\'Pronunciation playback failed\');});">'
            + SPEAKER + '</button>')


def front(theme):
    return ('<div class="sample-card theme-' + theme + ' side-front">'
            '<div class="word-block"><div class="word">{{Headword}}</div>'
            '<div class="forms">{{Details}}</div></div><div class="sound">{{Audio}}</div></div>')


def back(theme):
    # Deliberately omit FrontSide, German fields, audio, captions, and source credits.
    return ('<div class="sample-card theme-' + theme + ' side-back">'
            '<div class="meaning">{{English}}</div>'
            '{{#Image}}<div class="visual">{{Image}}</div>{{/Image}}</div>')


def main():
    sources = json.loads((ROOT / 'media-sources.json').read_text())
    images = {entry['card']: entry for entry in sources['images']}
    rows = re.findall(r'^\d+\. (.+?) — (.+)$', SOURCE.read_text(), re.M)[:10]
    assert len(rows) == 10
    cards = []
    for number, ((german, english), (word, details)) in enumerate(zip(rows, WORDS), 1):
        image = images.get(number)
        cards.append(dict(id=number, german=german, english=english, word=word,
                          details=details, speech=sources['audio']['spoken_text'][number-1],
                          image=image['file'] if image else '',
                          alt=image['description'] if image else '',
                          audio=f'a1_{number:03}_de.mp3'))
    for offset, (theme, name) in enumerate(THEMES):
        model = genanki.Model(1735068300 + offset, f'A1 Prototype — {name}',
            fields=[{'name': n} for n in ['ID', 'Headword', 'Details', 'English', 'Image', 'Audio', 'OriginalGerman', 'OriginalEnglish', 'SpokenGerman']],
            templates=[{'name': 'German → English', 'qfmt': front(theme), 'afmt': back(theme)}], css=CSS)
        deck = genanki.Deck(1735068310 + offset, f'German A1 · Preview · {name}')
        for card in cards:
            image = f'<img src="{card["image"]}" alt="{html.escape(card["alt"], quote=True)}">' if card['image'] else ''
            fields = [str(card['id']), html.escape(card['word']), html.escape(card['details']), html.escape(card['english']),
                      image, audio_button(card['audio']), html.escape(card['german']), html.escape(card['english']), html.escape(card['speech'])]
            deck.add_note(genanki.Note(model=model, fields=fields,
                          guid=genanki.guid_for('a1-design-prototype', theme, card['id']),
                          tags=['prototype', f'source_{card["id"]:03}']))
        package = genanki.Package(deck)
        package.media_files = [str(p) for p in sorted(MEDIA.iterdir()) if p.suffix in ('.mp3', '.jpg')]
        package.write_to_file(str(ROOT / f'first-10-{theme}.apkg'))
    (ROOT / 'cards.json').write_text(json.dumps(cards, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'cards.css').write_text(CSS)
    data = {**{theme: {'front': front(theme), 'back': back(theme)} for theme, _ in THEMES},
            'cards': cards, 'assets': {p.name: 'data:' + ('audio/mpeg' if p.suffix == '.mp3' else 'image/jpeg') + ';base64,' + base64.b64encode(p.read_bytes()).decode()
                                      for p in MEDIA.iterdir() if p.suffix in ('.mp3', '.jpg')}}
    page = (ROOT / 'preview-template.html').read_text()
    page = page.replace('/* CARD_STYLES */', CSS).replace('/* PROTOTYPE_DATA */', 'const DATA = ' + json.dumps(data, ensure_ascii=False) + ';')
    (ROOT / 'preview.html').write_text(page)
    print('Built the blue 10-card APKG deck and self-contained preview with click-only audio.')


if __name__ == '__main__':
    main()
