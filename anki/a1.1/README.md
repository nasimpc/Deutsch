# German A1.1 — approved Deck 01 visuals

528 cards in their original order across 18 numbered subdecks: Decks 01–17 contain 30 cards each; Deck 18 contains 18. Deck 01 has **16 approved images (4 animated GIFs)** and **14 deliberate gaps**. Decks 02–18 remain text/audio with no images. The user approved all 16 gallery proposals on 26 October 2026 (exact message: “approve all”); rejected candidates are excluded.

The blue design, German fronts, supplementary forms, English meanings and 525 original MP3 clips are preserved. Audio uses `de-DE-KatjaNeural`, 10% slower, and plays only when clicked. Backs contain the existing English meaning and optional approved image; all explanations, sources and credits remain outside study cards.

## Artifacts

- [german-a1.1.apkg](german-a1.1.apkg): rebuilt package with all media bundled offline.
- [preview.html](preview.html): self-contained offline study preview for all 528 cards, including embedded audio and animated images.
- [Candidate gallery](image-candidates/index.html): all 30 Deck 01 cards, exact chosen IDs, images, sources, rationale and gaps.
- [Canonical manifest](image-candidates/manifest.json): approved assignments keyed by stable card IDs, source URLs, approved asset hashes, exact approval and validation references. Historical batch files are research snapshots only.
- [verification.json](verification.json): current package checks and SHA256.
- [Research memory](../../docs/anki-deck-01-visual-research.md): actual searches, rejections, approval, integration evidence and handoff.

## Rebuild

With the existing environment/audio cache, no network is needed:

```sh
anki/a1.1/.venv/bin/python anki/a1.1/build.py prepare
anki/a1.1/.venv/bin/python anki/a1.1/build.py build
anki/a1.1/.venv/bin/python anki/a1.1/build.py verify
```

`prepare()` regenerates vocabulary/card data, while approved images remain in the separate persistent manifest. `build()` resolves only approved/integrated selections, checks the card/deck and exact asset hashes, copies them to media, and packages only referenced approved images plus all pronunciation clips. Keep `image-candidates/assets/` when rebuilding. Images survive repeated preparation/rebuilding, verified in [persistence.json](validation/persistence.json).

For a fresh environment or missing audio, `bash anki/a1.1/finish.sh` sets up pinned dependencies and generates any missing pronunciation clips before building. Completed audio is cached. Its `--setup-only` option checks environment setup.

## Import and compatibility

Import `german-a1.1.apkg` using Anki's Import command. The nine original field names/ordinals, model identity 1792936801, deck IDs, GUID convention and templates are unchanged. Approved image HTML follows the exact English meaning in the existing English answer field; no field was added. Vocabulary `cards.json` and original source fields remain unchanged.

An upgrade from the pre-image package was tested using default import options in disposable collections on Anki 25.02.5 (matching the installed app) and 26.9.3. All 528 existing notes/cards updated without duplicates; internal IDs, deck assignments, reviewed/lapsed intervals and suspension state were preserved. Repeating import added no duplicates or scheduler changes. See [25.02.5](validation/reimport-25-02-5.json) and [26.9.3](validation/reimport-26-9-3.json) reports. Personal Anki data was never accessed. Reimport into locally customized note types has not been tested.

## Validation

- Archive/database integrity; 528 distinct notes/cards; original source order, repeats and 18 deck sizes; exact approved image assignment; no images in gaps or Decks 02–18.
- [Preservation check](validation/preservation.json): all 525 MP3s byte-for-byte identical to the real old package; vocabulary, original fields, GUIDs, deck IDs, tags, field definitions and templates retained.
- [Negative checks](validation/verifier-negative-checks.json): verifier rejects images in Deck 02/gaps, wrong assignments, changed audio and autoplay; assignment resolver rejects other-deck images.
- [Offline browser check](validation/browser-verification.json): all 528 preview cards match exact German/English, all 16 images load, all 4 GIFs animate in gallery/preview/Anki-rendered answers, click-only audio plays, no JS errors or horizontal overflow at 390px.
- [Installed Anki client check](validation/anki-client-verification.json): imported all 528 cards into a disposable `/tmp` profile; all 4 GIFs visibly animate in Anki 25.02.5's AnkiWebView/QtWebEngine. Actual raster-frame differences and screenshots recorded.

AnkiMobile, AnkiDroid and the learner's personal collection/device have not been tested. Browser 390px checks simulate a small screen; they are not physical-device testing. Recording bytes are preserved; no claim of listening to all 525 recordings is made.
