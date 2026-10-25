# German–English Anki deck

## Agreed requirements

- Use the 683 pairs from `x-flashcards.md` as the source inventory. The current [vocabulary split plan](vocabulary-level-split.md) divides the study material into A1.1 and A1.2 using Netzwerk neu, permits splitting a mixed source pair into separate cards, and excludes material beyond A1.2. This supersedes the earlier requirement to include every complete pair.
- German on the front; only the English meaning and an optional mnemonic image on the back. Do not repeat German, grammar, audio, captions, or metadata on the back.
- Include German pronunciation audio for each vocabulary entry.
- Preserve the vocabulary details chosen during source conversion. Audit and correct the study content, retaining the original source fields for reference.
- The requested A1.1 build uses `x-flashcards-a1.1.md` as its study-card source and contains text and German pronunciation audio only. Do not include images in this build. This supersedes the earlier image requirement for the full build; the existing prototype still contains its three sample images.
- Bundled German pronunciation audio plays only when the speaker button is clicked. No automatic playback on either side.
- Selected design: option A, clean modern, with a blue palette. Remove the other two design options.

## First-ten-card sample

- Browser preview: `anki/prototype/preview.html`; includes all assets for offline viewing. Only the selected blue design remains.
- `anki/prototype/first-10-clean.apkg` contains ten forward cards, ten German MP3 recordings, and three JPEG images.
- The pronunciation field stores a complete HTML audio reference and a speaker button. No native sound tags or autoplay attributes are used, so playback requires a button click.
- Front: German headword, original supplementary forms, pronunciation. Back: English meaning and optional image only.
- Voice: `de-DE-KatjaNeural`, spoken 10% slower. Audio speaks the headword and noun article; both sender gender forms and alle/alles are included where applicable. Grammatical abbreviations are not spoken.
- Existing images: SpongeBob leaving (#3), Mean Girls pickup scene (#6), Leonardo DiCaprio pointing (#8). Source links are recorded in `media-sources.json`, outside the visible cards.
- The first ten prototype English meanings retain the source wording. The classified study lists include reviewed meaning corrections and split forms; these have not yet been applied to the prototype.

## Decisions to settle

The learner approved the following defaults on 25 October 2026:

- Preserve all **528 A1.1 cards**: 17 decks of 30, with 18 cards in the last deck. Do not add 12 cards merely to reach 540.
- Retain source order and repeated source entries.
- Deliver one `.apkg` containing 18 numbered subdecks, using the selected blue design.
- German on the front, English only on the back; no images.
- Bundle pronunciation for offline use, retaining the sample voice, speed and click-only playback.

The specific study device remains unspecified. Playback still needs checking in the learner's Anki installation.

## A1.1 build status

- [Complete text grouped into 18 decks](../anki/a1.1/decks.md), [browser preview](../anki/a1.1/preview.html), card data and resumable build scripts are prepared in `anki/a1.1/`.
- The source was checked against all 528 classified A1.1 records, including original fields and IDs.
- Six prototype audio clips match the approved spoken text. Another **519 unique clips** are needed; repeated identical spoken text shares an audio file.
- Audio synthesis is blocked by this execution environment's network restriction, and the permission request was rejected by the automatic approval policy. The final package has not been created.
- Package serialization and checks passed using temporary audio fixtures; those fixtures were discarded. Actual audio completeness and the final package will be checked after synthesis.
- [Completion instructions](../anki/a1.1/README.md) provide a single command to generate audio and build/verify the package from a terminal with internet access.

## Verified Anki capabilities

- [Packaged decks](https://docs.ankiweb.net/manual/importing/packaged-decks) import deck content and note types.
- [HTML and CSS templates](https://docs.ankiweb.net/manual/templates/styling) support custom card layouts, images, and audio replay styling.
- [Text-to-speech](https://docs.ankiweb.net/manual/templates/fields) can speak a dedicated German field, with voice availability depending on the platform.

The complete Anki deck has not been built; the current package is the selected blue design applied to the first ten source pairs. The current vocabulary split supplies **528 A1.1** and **178 A1.2** study-card records in the [two lists and provenance data](vocabulary-level-split.md), with splits, corrections and exclusions documented in the [audit](vocabulary-level-split-audit.md).
