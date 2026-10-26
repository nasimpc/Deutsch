# Deck 01 visual gallery — integrated

Open `index.html` directly in a browser. Previews use local assets, including four animated GIFs. Source links require internet.

All30 cards were searched. The user said **“approve all” on 26 October 2026**, approving the16 proposed visuals. All 16 are integrated in Deck 01; 14 gaps remain. Rejected 19-base-A and 41-base-A are excluded. Nothing was generated or newly captioned.

`manifest.json` is the canonical source and approved assignment record, keyed by stable card IDs. Its `assignments_approved` map persists independently of `prepare()`. Batch JSON and part-B Markdown retain historical research evidence; they are not assignment authorities. Extra asset renditions and rejected files are retained as evidence and are neither shown as choices nor packaged.

Re-render with `python3 anki/a1.1/image-candidates/build_gallery.py`.

`gallery-verification.json` is the historical Phase1 approval-gate check. Current integrated gallery/preview/Anki-rendered answer animation and mobile rendering checks are in `../validation/browser-verification.json`. Actual installed Anki GIF playback is in `../validation/anki-client-verification.json`. `source-link-checks.json` records32 successful source/asset links and a superseded404; `baseline.json` captures the original pre-image study package.

See `../README.md` for package, preview, reimport and validation details. The persistent research history is `docs/anki-deck-01-visual-research.md` at repository root. No personal Anki collection accessed; mobile clients untested.
