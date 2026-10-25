# First ten Anki cards — clean blue

Open `preview.html` in a browser. It is self-contained: pronunciation clips and the three existing images are embedded, so it works offline. Use the numbered buttons or keyboard left/right to select one of the ten entries, and the pronunciation button to play German audio. A dark preview toggle is available at the top.

Alternatively, import `first-10-clean.apkg` into Anki.

The selected design is option A in blue. The other two designs and their packages/screenshots have been removed. The sample has ten forward cards, ten bundled MP3 clips, and three existing JPEG images, separate from the future 683-card deck.

The answer template contains only the English meaning and the optional image. Source fields are retained in the notes but are not displayed. Exactly cards 3, 6, and 8 have an image. Images are unchanged downloads; the presentation uses CSS. Attribution/source links and the spoken text are recorded in `media-sources.json`.

The audio uses the German voice `de-DE-KatjaNeural` at 10% slower speed. It reads the vocabulary headword and, for nouns, its article, rather than reading grammatical abbreviations. Both the Anki card and browser preview play only when the front's speaker button is clicked. The Anki audio field uses an HTML audio element without autoplay, rather than a native automatic sound tag. Its full media reference is stored in the field for media checking and export.

## Rebuild

From the repository root, with `genanki` available in `.venv`:

```sh
.venv/bin/python anki/prototype/build.py
```

If the downloaded media needs to be recreated, run the following first. It requires internet access and uses a temporary Python environment for `edge-tts`:

```sh
UV_CACHE_DIR=/tmp/anki-uv-cache uv run --no-project --with edge-tts python anki/prototype/prepare_media.py
```

## Scope

This sample uses the selected visual layout. It does not perform the full vocabulary audit or build the remaining 673 cards. It has not yet been evaluated in the user's Anki installation.
