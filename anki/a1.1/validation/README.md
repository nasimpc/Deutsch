# Integration validation

Reports were produced on 26 October 2026 against the local real package. All test Anki collections are disposable; no personal collection was used.

- `baseline-content.json` and ignored `before-images.apkg`: actual pre-image schema,528 notes/GUIDs, original fields/tags/order/deck IDs and 525 MP3 hashes. The old package hash is `fc733c93bdb280d4a51de00b1b1570595178ca8a9b69a3c700dffe71fb944c72`.
- `preservation.json`: current package compared with baseline; only approved answer additions and image CSS permitted.
- `persistence.json`: second prepare/build/verify cycle preserves all 16 assignments and original cards.json.
- `verifier-negative-checks.json`: mutations in temporary packages rejected. No mutation tests touch the deliverable package.
- `reimport-25-02-5.json`, `reimport-26-9-3.json`: old package→image package→repeat import, default options. Internal note/card IDs, simulated reviewed/lapsed and suspended scheduler state remain intact; 528 cards,16 illustrated,no duplicates. `rendered-anki-cards.json` contains actual Anki-generated HTML for all 16 illustrated cards.
- `browser-verification.json`: isolated Chrome, external networking disabled, all 528 preview cards and all 16 package answers, exact text/assignment, click-only actual MP3 playback, 390px layout and four GIFs in gallery/preview/package answers. Screenshots: preview-mobile.png,preview-desktop.png,package-back-mobile.png.
- `anki-client-verification.json`: installed Anki 25.02.5 client, explicitly isolated `/tmp/a11-anki-client-*` base; all 4 GIFs visibly animate in AnkiWebView/QtWebEngine. Raster snapshots differ across frames. Screenshots `anki-*-base.png` show the actual Anki WebView.

Test scripts use stdlib plus genanki for package verification, anki for reimport, and playwright/installed Chrome for browser checks. `anki_client_addon.py` is a temporary harness that refuses personal profile paths; do not install it in a personal profile. Backend versions25.02.5 and 26.9.3 were installed in temporary environments. GIF source/package bytes are checked independently by SHA256.

Client-test investigation: first isolated app launch stopped at first-run language setup; it was terminated before creating a collection, then a separate preconfigured temporary profile was used. Canvas drawImage initially yielded a fixed GIF frame and did not establish animation; switching to actual QtWebView raster captures verified visible motion. A startup update-dialog callback emitted a shutdown warning after the test closed; test results/screenshots were already recorded. No personal Anki data or settings used.

Limits: AnkiMobile/AnkiDroid, physical-device behavior and locally customized personal note types are unverified. Reimport tests cover unchanged note types with simulated scheduling edits; all 525 original audio bytes are preserved, not all recordings listened to.
