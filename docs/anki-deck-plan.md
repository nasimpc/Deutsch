# German–English Anki deck

## Agreed requirements

- Use the 683 pairs from `x-flashcards.md` as the source inventory. The current [vocabulary split plan](vocabulary-level-split.md) divides the study material into A1.1 and A1.2 using Netzwerk neu, permits splitting a mixed source pair into separate cards, and excludes material beyond A1.2. This supersedes the earlier requirement to include every complete pair.
- German on the front; only the English meaning and an optional mnemonic image on the back. Do not repeat German, grammar, audio, captions, or metadata on the back.
- Include German pronunciation audio for each vocabulary entry.
- Preserve the vocabulary details chosen during source conversion. Audit and correct the study content, retaining the original source fields for reference.
- The A1.1 build uses `x-flashcards-a1.1.md`: 528 source cards with German audio. On 26 October 2026 the user approved all 16 proposed Deck 01 visuals, including 4 GIFs. 14 Deck 01 gaps remain; Decks 02–18 have no images. This supersedes the earlier text/audio-only requirement for Deck 01 only.
- Bundled German pronunciation audio plays only when the speaker button is clicked. No automatic playback on either side.
- Selected design: option A, clean modern, with a blue palette. Remove the other two design options.

## Deck 01 visual research authorization — 25 October 2026

The [Deck 01 image brief](anki-deck-01-image-goal-prompt.md) supersedes the no-images decisions below **only for German A1.1::Deck 01**. Search all 30 existing cards, present an offline candidate gallery, and wait for individual selections before integrating. Decks 02–18 retain text/audio content with no images. Current proposals and evidence live in the [research memory](anki-deck-01-visual-research.md). The user subsequently said **“approve all” on 26 October 2026**: all 16 proposed candidates are approved and integrated. Rejected candidates are excluded; 14 gaps preserved.

## First-ten-card sample

- Browser preview: `anki/prototype/preview.html`; includes all assets for offline viewing. Only the selected blue design remains.
- `anki/prototype/first-10-clean.apkg` contains ten forward cards, ten German MP3 recordings, and three JPEG images.
- The pronunciation field stores a complete HTML audio reference and a speaker button. No native sound tags or autoplay attributes are used, so playback requires a button click.
- Front: German headword, original supplementary forms, pronunciation. Back: English meaning and optional image only.
- Voice: `de-DE-KatjaNeural`, spoken 10% slower. Audio speaks the headword and noun article; both sender gender forms and alle/alles are included where applicable. Grammatical abbreviations are not spoken.
- Existing images: SpongeBob leaving (#3), Mean Girls pickup scene (#6), Leonardo DiCaprio pointing (#8). Source links are recorded in `media-sources.json`, outside the visible cards.
- The first ten prototype English meanings retain the source wording. The classified study lists include reviewed meaning corrections and split forms; these have not yet been applied to the prototype.

## Original defaults — 25 October 2026

The learner approved the following defaults on 25 October 2026:

- Preserve all **528 A1.1 cards**: 17 decks of 30, with 18 cards in the last deck. Do not add 12 cards merely to reach 540.
- Retain source order and repeated source entries.
- Deliver one `.apkg` containing 18 numbered subdecks, using the selected blue design.
- German on the front, English on the back; the original no-images rule was superseded for approved Deck 01 images on 26 October 2026.
- Bundle pronunciation for offline use, retaining the sample voice, speed and click-only playback.

The specific study device remains unspecified. Playback still needs checking in the learner's Anki installation.

## A1.1 build status — 26 October 2026

- [Package](../anki/a1.1/german-a1.1.apkg), [offline preview](../anki/a1.1/preview.html), [gallery](../anki/a1.1/image-candidates/index.html), [approved source manifest](../anki/a1.1/image-candidates/manifest.json) and [verification](../anki/a1.1/verification.json) are complete.
- 528 cards/18 subdecks/525 original MP3s/16 approved images/4 animated GIFs/14 Deck 01 gaps; Decks 02–18 unchanged and image-free. Audio remains click-only.
- Existing nine-field schema, model identity, templates, GUIDs and deck IDs preserved; approved image HTML is appended only to the existing English answer field.
- Two preparation/build cycles passed. Negative checks reject unintended images and altered/autoplay audio. Offline preview and actual Anki-rendered answers passed mobile-width and animation checks.
- Reimport from the real old package passed without duplicates or scheduling changes in disposable collections on Anki 25.02.5 and 26.9.3. Installed Anki 25.02.5 AnkiWebView played all 4 GIFs in an isolated profile. [Validation reports](../anki/a1.1/validation/README.md).
- Personal collection and mobile clients were not tested. See [current README](../anki/a1.1/README.md) for limitations and reproduction commands.

## Verified Anki capabilities

- [Packaged decks](https://docs.ankiweb.net/manual/importing/packaged-decks) import deck content and note types.
- [HTML and CSS templates](https://docs.ankiweb.net/manual/templates/styling) support custom card layouts, images, and audio replay styling.
- [Text-to-speech](https://docs.ankiweb.net/manual/templates/fields) can speak a dedicated German field, with voice availability depending on the platform.

The complete A1.1 text/audio deck has been built and verified; the separate prototype remains the selected blue design applied to the first ten source pairs. The current vocabulary split supplies **528 A1.1** and **178 A1.2** study-card records in the [two lists and provenance data](vocabulary-level-split.md), with splits, corrections and exclusions documented in the [audit](vocabulary-level-split-audit.md).
