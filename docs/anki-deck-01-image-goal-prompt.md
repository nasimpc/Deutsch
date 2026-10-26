# Codex goal prompt: memorable images for German A1.1 Deck 01

Copy the following prompt into Codex:

---

Add carefully selected, existing mnemonic visuals to the first subdeck of my German–English Anki deck. Static images and animated GIFs are both allowed; references to “images” below include both. Work in `/Users/muhammednasim/Desktop/a1`.

## Goal and scope

Target only `German A1.1::Deck 01`, the first 30 cards in `anki/a1.1/`. Search for an image for every card, but use only strong matches. Leave a card without an image when the available options are weak. Preserve all 528 cards, their order, repeated entries, and the 18-subdeck structure. Decks 02–18 must keep their existing study content and have no images.

This instruction supersedes the earlier “no images” requirement in `docs/anki-deck-plan.md` and `anki/a1.1/README.md` for Deck 01 only. It does not authorize changing the vocabulary, meanings, or audio.

Read the plan, card data, builder, preview, prototype image implementation, and applicable repository instructions first. Verify current artifacts: `anki/a1.1/german-a1.1.apkg` and `verification.json` were found during planning, although the documentation says the package is unfinished. Establish the actual current state before changing anything.

## My image preferences

My favorite quality is a memorable connection between the **German word and its English meaning**. Funny cartoons, memes, recognizable movie scenes, and animated GIFs are welcome. Text within an existing image or GIF is allowed. Choose stills or GIFs based on the strength of the memory connection; motion is useful when it makes an action or scene easier to remember.

Prefer an image that makes the German expression lead to its meaning, using a sound association, visual pun, or fitting scene. For example, a funny hunting dog could connect *Hund* with “dog” through “hunt.” This is an illustration of the mnemonic approach; *Hund* is not an extra card to add.

Rank candidates by:

1. Strength of the German-to-English memory connection.
2. Clarity and accuracy of the meaning being learned.
3. Humor, surprise, and memorability.
4. Legibility on a small Anki card.

A funny scene that merely depicts the English meaning is a fallback, and should be labeled as such. An unrelated popular meme is not useful. Do not invent a strained explanation to justify a weak match. Sound associations are memory aids, not pronunciation guidance or etymology; preserve the real German pronunciation audio.

Distinguish related entries deliberately, such as `anfangen` / `der Anfang`, `sich anmelden` / `die Anmeldung`, and `antworten` / `die Antwort`. Each candidate should help retrieve that card's entry. Abstract words can remain gaps when no clear connection exists.

**Do not generate images, GIFs, or animations, or call image-generation tools.** Do not fabricate meme panels, draw replacement illustrations, or add new text to images. Find existing images and animated GIFs, including existing captioned memes. Simple resizing, format conversion, and cropping are allowed when they preserve the relevant scene and text. Preserve animation for selected GIFs; do not silently replace them with static frames.

## Phase 1: research and a reviewable candidate gallery

Read `docs/anki-deck-01-visual-research.md` before researching. Maintain it as the persistent Markdown research memory: after each search batch, record exact queries, inspected source links, candidate IDs, local asset paths, mnemonic reasoning, rejected options, failed searches, and remaining gaps. Keep its card tracker and handoff current, and record my selections when received. Follow the record formats in that file so future agents can resume without repeating completed work. Reuse candidate identifiers consistently across the report, gallery, and manifest. Record only research actually performed; label uninspected or uncertain findings explicitly.

Use web and image search to find actual candidates. Inspect the images themselves and their source pages; do not select from search snippets alone. Use original or reliably attributed sources where available. Record both the source-page URL and image URL, along with available creator, film, or usage information. If an image cannot be retrieved or inspected, mark it as unresolved rather than claiming it is ready.

Create a local gallery, preferably `anki/a1.1/image-candidates/index.html`, covering all 30 cards in their existing order. Include:

- The exact German entry and English meaning from the current card data.
- One recommended image and up to two genuinely useful alternatives, when available.
- Actual image previews (animated for GIF candidates), clear candidate identifiers, asset type and file size, and source links.
- A short explanation of how the image connects the German word to the English meaning.
- Whether it is a German-word mnemonic or a meaning-only fallback, plus any ambiguity.
- An explicit gap entry when no strong candidate was found.

Keep the gallery and research explanations separate from study-card content. Download gallery assets for offline review where possible. Store candidate records in a machine-readable manifest keyed by stable card IDs so the work is resumable. Do not change study-card image assignments or rebuild the deck with unapproved candidates during this phase.

Review the gallery for image visibility, correct card matching, readable text, and working source links. Present its local path, summarize the strongest candidates and remaining gaps, and ask me to choose or approve images using the candidate identifiers.

**Stop at this approval gate.** Approval of this prompt authorizes the research and gallery, not acceptance of individual images. Keep the integration work pending until I select or approve candidates. Do not mark the overall goal complete at the gallery stage.

## Phase 2: integrate the approved selections

After my approval, bundle the selected images locally for offline use, add them to the corresponding Deck 01 card backs, update the browser preview, and rebuild and verify the Anki package. Preserve the blue design, German fronts, supplementary forms, pronunciation buttons, English meanings, and click-only audio. The study-card back should contain only its existing English meaning and optional approved image; no extra German labels, visible mnemonic explanations, source credits, or research metadata. Existing text within the selected image is allowed. Keep attribution and explanations in the external manifest or documentation.

Inspect the existing prototype for reusable image rendering and media bookkeeping. The A1.1 builder currently has audio-only packaging and validation; update them to permit approved images while retaining audio checks. `prepare()` rewrites `cards.json`, so keep image selections in a separate persistent manifest or otherwise ensure they survive preparation and rebuilds.

Preserve stable card IDs, note GUIDs, deck IDs, model identity, existing field order, and scheduling compatibility. The current GUID convention is `genanki.guid_for('german-a1.1-study', card['card_id'])`; the model ID is `1792936801`, and numbered deck IDs derive from `1792936900`. If an image field is needed, append it after existing fields. Inspect the actual schema before editing. Validate reimport behavior in an isolated Anki collection if the available environment permits it; matching GUIDs alone does not establish safe updating after a schema change. Do not modify my personal Anki collection. Clearly report any import behavior that could not be verified.

## Completion criteria

- Only my approved images appear, exclusively in Deck 01, with intentional gaps preserved.
- The package still contains 528 cards across the same 18 subdecks; Deck 01 has 30 cards.
- Existing vocabulary, meanings, ordering, identifiers, and bundled German audio are preserved.
- Image assignments survive preparation and rebuilding.
- All referenced audio and image assets are packaged and work offline; audio remains click-only.
- Approved GIFs are bundled as local animated assets, retain their animation, and animate in the offline gallery and browser preview. Check animation in Anki where available and report any unverified client behavior. Use reasonably sized files that remain readable.
- Image display works in the browser preview and the package templates, with readable proportions on small screens.
- Package verification checks approved image assignments and detects unintended images in Decks 02–18.
- The local gallery, source manifest, updated preview, rebuilt `.apkg`, and verification results are available at clearly stated paths.
- `docs/anki-deck-01-visual-research.md` contains the actual search history, candidate evidence, rejection reasons, user selections, unresolved gaps, and a current handoff for future agents.
- Relevant documentation accurately reflects the completed work and any remaining device or import validation limits.

Report the final number of illustrated cards, remaining gaps, artifact paths, checks performed, and any specific unresolved limitation. Do not claim images were generated or that device testing occurred unless it actually did.
