# German A1.1 — text and audio

Approved on 25 October 2026: one Anki package with 18 numbered subdecks, in the order of `x-flashcards-a1.1.md`. Decks 01–17 each contain 30 cards; Deck 18 contains 18. All 528 source cards, including repeated source entries, are retained. No additional vocabulary or images are added.

The front shows German, its supplied supplementary forms and a pronunciation button. The back shows only the English meaning. The blue design is retained. Audio uses `de-DE-KatjaNeural`, 10% slower, and plays only when clicked. It reads headwords, noun articles and lexical alternatives; dictionary plural annotations and grammatical labels are not read. MP3 files will be bundled for offline use.

## Current status

- All 528 cards have been converted and checked against the classified source and original fields.
- [decks.md](decks.md) contains the complete text grouped into the 18 decks.
- [preview.html](preview.html) previews every card offline. Six matching prototype recordings are available; other pronunciation buttons are disabled until audio is generated.
- The cards require 525 unique recordings. Six were reused; **519 remain to be generated**. Identical spoken text shares a recording, while repeated source cards remain separate.
- The execution environment cannot reach the speech service; its approval policy rejected the request for network access.
- **The final `german-a1.1.apkg` has not been created.** The builder refuses to create it until every recording exists.

## Complete the package

Run from a terminal with internet access:

```sh
bash anki/a1.1/finish.sh
```

The script creates a local Python environment, installs the pinned dependencies, generates the missing audio, builds `german-a1.1.apkg`, refreshes the preview and checks the package. Completed clips are cached, so rerunning resumes interrupted audio generation.

Activation is optional because the script invokes the environment's Python directly. To activate it for manual commands, run `source anki/a1.1/.venv/bin/activate`. If an earlier setup failed, leave it inactive while rerunning `finish.sh`; the script automatically rebuilds incomplete environments using the resolved Python installation path. Run `bash anki/a1.1/finish.sh --setup-only` to check just the environment and pip without downloading dependencies or generating audio.

Once built, import `german-a1.1.apkg` using Anki's Import command. It contains `German A1.1::Deck 01` through `German A1.1::Deck 18`. Study order follows the source when Anki is configured to introduce new cards in order. Device playback has not yet been tested in the learner's Anki installation.

## Validation

The package builder was exercised in a temporary directory using an existing MP3 as a structural test fixture. Checks passed for 528 distinct notes and forward cards, all source fields and translations, source order, the 18 deck sizes, bundled media references, English-only answers, and absence of images and autoplay. The fixture package and audio were discarded; this does not validate recordings that have not been generated.

The real build will write `verification.json` only after checking the completed package. To repeat that check:

```sh
anki/a1.1/.venv/bin/python anki/a1.1/build.py verify
```
