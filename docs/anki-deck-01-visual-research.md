# Deck 01 visual research memory

## Current handoff

- Completed 2026-10-26: all 30 Deck 01 cards searched; user approved all 16 proposed gallery candidates (exact message **“approve all”**). All 16 are integrated, including 4 animated GIFs; 14 deliberate gaps remain. Rejected 19-base-A and 41-base-A are excluded.
- Canonical [manifest](../anki/a1.1/image-candidates/manifest.json) records selected_candidate_id, exact approval, packaged filenames, approved hashes and current integration checks. Research batch files are historical snapshots only.
- Deliverables: [package](../anki/a1.1/german-a1.1.apkg), [offline study preview](../anki/a1.1/preview.html), [gallery](../anki/a1.1/image-candidates/index.html), [verification](../anki/a1.1/verification.json), [validation reports](../anki/a1.1/validation/README.md).
- Verified 528 cards/18 original subdecks/525 unchanged MP3s. Only 16 approved answer-image additions, all in Deck 01; Decks 02–18 and intentional gaps have no images. Source text, repeats, order, GUIDs, fields/ordinals, model identity, templates and deck IDs retained.
- No new field: approved image HTML follows the exact English meaning in the existing English field. Blue CSS uses existing .visual rules, with max image height 420px. Persistent assignments survive prepare/build twice.
- Offline Chrome checked all 528 preview cards and all 16 actual Anki-rendered answers; all 4 GIFs animate in gallery, preview and package answers, audio plays only on click, 390px layout has no overflow. Actual installed Anki 25.02.5 AnkiWebView also animated all 4 GIFs in a disposable profile.
- Reimport old→new→repeat passed with default options on isolated Anki 25.02.5 and 26.9.3 collections: no duplicates, internal IDs and simulated reviewed/lapsed/suspended scheduler state preserved.
- Remaining validation limits: no personal collection access; AnkiMobile/AnkiDroid, physical-device behavior and locally customized note types untested. No additional approval needed for the integrated selections.
- Next action: user can import the package or open the offline preview. Future image/content changes require a new explicit request; retain this research history and manifest.

## Confirmed preferences

The user confirmed the brief in this conversation on 2026-10-25 and subsequently allowed animated GIFs.

- Existing funny cartoons, memes, movie scenes, and animated GIFs are welcome.
- Highest priority: a memorable connection from the German word to its English meaning. Sound associations and visual puns are allowed. Meaning-only illustrations are a fallback.
- Existing text inside visuals is allowed.
- Search all 30 cards; leave gaps rather than fill them with weak candidates.
- Find existing visuals; no image, GIF, or animation generation. Preserve animation for approved GIFs.
- Present candidates in a gallery for the user's selection before integration. Approval of the task brief is not approval of any candidate.
- Keep image additions within Deck 01 and preserve the vocabulary, meanings, audio, and other subdecks.

## How to maintain this memory

1. Read this file before searching, downloading, choosing, or integrating visuals. Resume from recorded findings and unresolved items.
2. After each search batch, record the exact queries, sources inspected, candidates, rejected options, and failures. Save before a handoff or interruption.
3. Use stable `card_id` values from card data. Give every candidate a permanent identifier such as `1-base-A`; use that same identifier in the gallery and machine-readable manifest. Keep identifiers stable if rankings change.
4. Distinguish observations from mnemonic suggestions. A search thumbnail is not proof that the full asset was inspected; a proposed connection is not a user-approved choice.
5. Update the tracker, decision history, and current handoff after discoveries or user feedback. Retain rejection reasons and superseded decisions so later agents can understand them.
6. Before retrying a failed source or rejected query, read the reason and state what changed. Recheck expired or broken links when needed.
7. Store source, candidate, gallery, and local asset references here. Keep exact integration assignments in the machine-readable manifest described by the goal prompt, and reconcile any disagreement before building.

## Card tracker

| Position | Stable card ID | German | English | Status | Candidate IDs / notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `1-base` | ab (ab heute) | from (from today) | Gap | No strong visual for the temporal from (from today) surfaced. Departure pictures would teach a different use of ab. |
| 2 | `2-base` | aber | but | Gap | Classroom clauses and generic reaction memes do not create a clear aber → but cue; no forced bear/butt association. |
| 3 | `6-base` | abholen | to pick up / collect | Integrated | `6-base-A` |
| 4 | `8-base` | Achtung! | attention! / watch out! | Integrated | `8-base-A` |
| 5 | `9-base` | die Adresse, Adressen | address | Integrated | `9-base-A` |
| 6 | `10-base` | alle / alles | all (everything) | Integrated | `10-base-A` |
| 7 | `11-base` | allein | alone | Integrated | `11-base-A` |
| 8 | `12-base` | also | so, thus | Gap | No clear therefore/so visual with a German cue; English also creates a false-friend risk. |
| 9 | `13-base` | alt | old | Integrated | `13-base-A` |
| 10 | `14-base` | das Alter | age, old age | Integrated | `14-base-A` |
| 11 | `15-base` | an | on (adv), at (prep) | Gap | Switch results mostly encode EIN or I/O; a single switch also misses at. No useful unified cue. |
| 12 | `17-base` | das Angebot, Angebote | offer | Integrated | `17-base-A` |
| 13 | `18-base` | anderer / andere / anderes | other | Gap | Search returned unrelated wanderer memes; no clear other contrast with a German cue. |
| 14 | `19-base` | anfangen | to start | Gap | Bugs Bunny GIF was inspected but loops dancing at a START sign without actually starting. Rejected rather than claiming the action; der Anfang has a separate noun fallback. |
| 15 | `20-base` | der Anfang | start | Integrated | `20-base-A` |
| 16 | `21-base` | anklicken (etw. Akk.) | to click something | Integrated | `21-base-A` |
| 17 | `24-base` | ankreuzen | to tick / mark with a cross | Integrated | `24-base-A` |
| 18 | `26-base` | sich anmelden (Akk.) | to register / enrol | Gap | No strong inspected registering/enrolling action; login screenshots teach a different sense and dense forms are illegible. Kept distinct from noun Anmeldung. |
| 19 | `27-base` | die Anmeldung | application, registration | Gap | No memorable, readable application/registration-result visual; dense full-page municipal forms rejected. Kept distinct from verb sich anmelden. |
| 20 | `28-base` | die Anrede | form of address | Gap | No clear form-of-address visual. Generic Herr/Frau tables are text-heavy; animal honorific cartoon teaches different words. |
| 21 | `29-base` | anrufen | to telephone | Gap | No strong German cue or humorous outgoing-call scene. Generic rotary dialing is bland; Mr Bean phone conversation retained only for noun Anruf, direction unspecified. |
| 22 | `30-base` | der Anruf, Anrufe | telephone call | Integrated | `30-base-A` |
| 23 | `31-base` | der Anrufbeantworter | answering machine | Gap | No strong inspected phone-call-answerer mnemonic. Generic icon/photo might retrieve telephone or tape recorder; Friends dialogue needs audio and shows no machine. |
| 24 | `34-base` | antworten | to answer | Gap | No clear visual of answering a question. Hermione hand raise can mean volunteering; ant-word sound association found no existing fitting scene. Kept distinct from noun Antwort. |
| 25 | `35-base` | die Antwort, Antworten | answer | Integrated | `35-base-A` |
| 26 | `36-base` | die Anzeige, Anzeigen | advertisement | Gap | Fry paying depicts buying rather than advertisement. Old Spice scene needs ad recognition; slang classified ad has incorrect German and tiny text. No strong inspected candidate. |
| 27 | `39-base` | der Apfel, Äpfel | apple | Integrated | `39-base-A` |
| 28 | `40-base` | der Appetit | appetite | Integrated | `40-base-A` |
| 29 | `41-base` | arbeiten | to work | Gap | Inspected work/money meme rejected: talking heads show no work; multi-sentence German joke too demanding. Kept distinct from noun Arbeit. |
| 30 | `42-base` | die Arbeit, Arbeiten | work | Integrated | `42-base-A` |

## Search log

### Search S001 — 2026-10-25

- Card IDs: `1-base`, `2-base`, `6-base`, `8-base`.
- Search tool / site: web search.
- Exact queries: `German ab heute meme from now on`; `German aber meme but`; `Mean Girls get in loser going shopping pickup meme`; `Achtung sign funny German`.
- Pages inspected: none yet; discovery results only. Tenor result https://tenor.com/view/mean-girls-shopping-gif-23164018 and existing prototype Imgflip source will be inspected next.
- Candidates discovered: none ready yet.
- Rejected results / unsuccessful searches: no usable direct German-word association surfaced for ab/aber; do not treat this as exhaustive.
- Access failures: none observed.
- Next useful query or source: inspect pickup scene and German warning signs with embedded Achtung.

### Baseline audit — 2026-10-25

- Read plan, cards, builder, preview template, prototype builder/template and media sources, README, CONTEXT. No applicable AGENTS.md found in repository or ancestor paths.
- Ran `python3 anki/a1.1/build.py verify`: PASS on the real existing package, 528 cards / 18 subdecks / 525 bundled MP3s / 0 images / click-only template audio.
- Package SHA256 `fc733c93bdb280d4a51de00b1b1570595178ca8a9b69a3c700dffe71fb944c72` matches prior report. README/plan claims of an unfinished package are stale.
- Baseline hashes, exact Deck 01 inventory and existing nine-field schema recorded in `anki/a1.1/image-candidates/baseline.json`. No model or study content changed. Prototype conditional Image rendering and .visual CSS are reusable, but its field order differs; do not copy its model schema.
- Research skill delegates positions 16–30 to a background researcher; its S101+ logs will be merged here.

### Search S002 — 2026-10-25

- Card IDs: `8-base`, `10-base`, `11-base`; exploratory rejection for `2-base`.
- Search tool / site: web image search and web search.
- Exact queries: `Achtung lustiges Schild Enten`; `allein Home Alone Kevin meme`; `site.imgflip.com all the things meme`; `site.imgflip.com one does not simply but meme`.
- Pages inspected: image-search previews only so far. Discovered original retailer https://schildbruder.de/produkt/schilder/schild-achtung-enten/ and original comic https://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html (opening next).
- Candidates discovered: warning sign, Home Alone scene and All the Things comic are leads, not ready assets.
- Rejected results: duck sign with gun caption is cluttered and unrelated; Boromir template does not encode aber/but and is rejected. Generic Kevin scream encodes surprise unless film-title association is made explicit.
- Access failures: none yet.
- Next useful source: inspect original comic and retailer; search existing German film title.

### Search S003 — 2026-10-25

- Card IDs: `1-base`, `2-base`, `6-base`, `8-base`, `9-base`, `10-base`.
- Tool: web image search / source-page opens.
- Exact queries: `aber but German meme`; `ab heute meme`; `Harry Potter Hogwarts envelope address`.
- Pages inspected: https://schildbruder.de/produkt/schilder/schild-achtung-enten/ (retailer, direct German warning label); https://tenor.com/view/mean-girls-shopping-gif-23164018 (Mean Girls pickup GIF, uploader blupanderz); https://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html (Allie Brosh original comic; images need HTML extraction).
- Candidates: `8-base-A` downloaded, not full-visual-inspected yet. Harry Potter address prop lead https://www.juliensauctions.com/en/items/112355/harry-potter-and-the-sorcerer-s-stone-hogwarts-invitation-envelope-prop (image preview only).
- Rejected: aber classroom slide has long text, weak visual retrieval; wenn/aber cartoon has conditional grammar unrelated to but; no strong ab heute lead.
- Access failures: default Python urllib DNS failed; identical download with approved network escalation succeeded (70923 bytes). Not an image-quality failure.
- Next: full image inspection and source downloads.

### Search S004 — 2026-10-25

- Card IDs: `11-base`, `12-base`, `13-base`, `14-base`, `15-base`.
- Tool: web image and web search.
- Exact queries: `alt old man Up Carl meme`; `das Alter Geburtstag 100 Kerzen`; `an aus Schalter beschriftet`; `site.disneyplus.com "Kevin" "allein"`; `"also" "so" "meme" German`.
- Pages inspected: discovery results only. Disney+ official German title supports Kevin–Allein zu Haus association (page to open); 100th-birthday candles lead from original retailer Celebration Stadium.
- Candidates discovered: none ready yet.
- Rejected/unsuccessful: no useful also/so retrieval; false English also association risks wrong meaning. Multisearch image output mostly returned birthday results, so alt/an need targeted follow-up.
- Access failures: no new failures.
- Next: individual image queries for switch/old man; German film-title artwork.

### Search S005 — 2026-10-25

- Cards: `17-base`, `18-base`, `19-base`, `20-base`.
- Tool: web image search.
- Exact queries: `"Angebot" "Pate" meme`; `"anderer" "meme"`; `"anfangen" "Start"`; `"Anfang" "Startlinie"`.
- Inspected: image-search previews only; source pages opening in S006.
- Leads: German Godfather caption https://www.meme-arsenal.com/en/create/meme/3355963 (`17-base-A`, provisional); bare track start line https://www.midliferun.today/blog/2017/7/21/cim-training-the-beginning-its-time-to-sweat-again (`20-base-A`, provisional meaning-only).
- Rejected: anfangen conjugation tables are reference material, no useful scene; other/anderer query returned unrelated Genshin wanderer pictures, no genuine mnemonic. Angebot desert cartoon by Karsten Schley has long dialogue less legible than Godfather caption; not retained as alternative.
- Failure: no strong anfangen action scene from this query; next search starter GIF.

### Search S006 — 2026-10-25

- Cards: `9-base`, `11-base`, `13-base`, `14-base`, `15-base`, `17-base`, `20-base`.
- Exact image queries: `"an" "aus" "Schalter"`; `"alt" "Carl" "Oben"`; `"Kevin allein zu Haus" poster`.
- Source pages opened: https://www.meme-arsenal.com/en/create/meme/3355963 confirms existing German caption; https://www.juliensauctions.com/en/items/112355/harry-potter-and-the-sorcerer-s-stone-hogwarts-invitation-envelope-prop rendered only navigation/title (prop description unresolved); https://celebrationstadium.com/pages/100th-birthday-party-ideas redirects to /password (reject as ready source); https://www.midliferun.today/blog/2017/7/21/cim-training-the-beginning-its-time-to-sweat-again opens with blog and photo; https://www.disneyplus.com/de-de/browse/entity-45e4a68f-d9df-45f7-8e81-01b4ca5524e9 official German film title and synopsis confirms allein/alone.
- Leads: German Kevin poster via IMDb / Thalia cinema; source image will be downloaded and inspected. Carl search mostly cluttered film posters (reject); switch query did not surface useful results (retry individually).
- No approvals.

### Search S007 — 2026-10-25

- Cards: `6-base`, `9-base`, `10-base`, `11-base`, `13-base`, `14-base`, `15-base`, `19-base`.
- Exact queries: image `German Ein Aus Schalter an aus`; web `site.tenor.com "start" "race"`; web `site.pixar.com "Carl" "Up"`; web `"Alter" "Geburtstag" "Cartoon"`; image `"anfangen" "los geht" meme`; image `"Alter" "Geburtstag" lustig cartoon`.
- Opened sources: https://propstore.com/product/harry-potter-and-the-philosophers-stone-2001/lot-164-hero-wax-sealed-hogwarts-acceptance-letter/ (real movie prop envelope); https://www.thalia-potsdam.de/einmalig/adventskino/ (cinema source poster); https://www.pixar.com/upfilm (original Carl character portrait); https://tenor.com/search/start-line-gifs (scene discovery).
- Downloads: `17-base-A` German Godfather, `11-base-A` German Kevin poster, `9-base-A` envelope, `20-base-A` bare START line. HTML retrieved for original Allie Brosh comic, Pixar character page, Tenor pickup GIF; full visual inspection next.
- Rejections: on/off switch often labeled EIN or I/O, does not cue an and omits at; leave an gap. Birthday cartoon referencing Third Reich is distracting to age retrieval; long card greetings also weak. No full visual inspected for these rejected thumbnails.
- Access failures: Tenor image click and Disney image click produced web Internal Error; direct Tenor asset extracted successfully from source HTML (download pending). Celebration Stadium source password-locked, not used.
- Next: source-native cartoon/GIF inspection, distinguish start verb action from noun start line.

### Search S008 — 2026-10-25

- Cards: `6-base`, `8-base`, `9-base`, `10-base`, `11-base`, `13-base`, `14-base`, `17-base`, `19-base`, `20-base`.
- Exact web query: `site.tenor.com/view "start" "Bugs-Bunny" "Ready-Start"`.
- Source inspected: https://www.kartenparadies.at/products/geburtstag-lass-es-mal-richtig-krachen confirms Edition Basic Funny-live-series card, hippo inner motif. Downloaded its existing picture with Alter in caption. Direct source HTML for https://tenor.com/view/start-bugs-bunny-ready-start-run-gif-13506050 retrieved by urllib despite web cache miss; extracted real GIF.
- Actual full visuals inspected using view_image: warning sign, German Godfather caption, German Kevin poster, Hogwarts addressed envelope, Allie Brosh Clean All the Things, Pixar Carl portrait, hippo in old age, START track line. Pickup GIF inspected at frames 0/2/4 (5 frames total); Bugs GIF frames 0/4/9/13 (14 total) inspected next.
- Candidate IDs: `6-base-A`, `8-base-A`, `9-base-A`, `10-base-A`, `11-base-A`, `13-base-A`, `14-base-A`, `17-base-A`, `19-base-A`, `20-base-A`. Details and measured metadata in manifest/candidate records.
- Transformations: Carl, hippo and track JPEGs resized to maximum 1200px with unchanged aspect ratio and scene/text; GIF bytes untouched. No new imagery or captions.
- Rejections: scary Kevin frame alone dropped in favor of German-title poster; generic Leo pointing from prototype less exact than Achtung sign; no forced phonetic puns for abstract entries.
- Access failures: Tenor web open cache miss; direct source request succeeded and title/description inspected in HTML. Browser offline playback validation pending.

# Deck 01 visual research — positions 16–30

### Search S101 — 2026-10-25

- Card IDs: `21-base`, `24-base`.
- Search tool/site: web search and image search.
- Exact queries: image: `anklicken maus klick gif`; `ankreuzen Kreuz Kästchen`. Web: `site.tenor.com clicking mouse gif`; `site.commons.wikimedia.org ballot cross box`.
- Pages inspected: not yet; results include [Clicking Mouse](https://tenor.com/view/clicking-mouse-gif-25181352) and [tick symbols](https://omgsymbol.com/tick/).
- Candidates discovered: unresolved clicking GIF; no candidate selected yet.
- Rejected results: cross-stitch, decorative anchors, ballot-box photos do not illustrate marking a box.
- Access failures: none yet.
- Next action: open individual clicking GIF source and inspect; seek actual crossed ballot or checkbox.

### Search S102 — 2026-10-25

- Card IDs: `26-base`, `27-base`, `28-base`, `29-base`.
- Search tool/site: web and image search.
- Exact queries: web: `sich anmelden registration meme german`; `die Anmeldung registration form German image`; `die Anrede Herr Frau comic`; `site.tenor.com anrufen telephone mr bean`. Image: `anrufen mr bean telephone gif`; `ankreuzen Kästchen Kreuz`; `sich anmelden Einschreibung cartoon`; `die Anmeldung Formular`.
- Results inspected at search-result level: [Anmeldung form](https://allaboutberlin.com/docs/anmeldung); [Anrede Duden sample PDF](https://shop.duden.de/media/c2/7d/84/1687427757/Leseprobe_9783411740444_Digital_erfolgreich_kommunizieren.pdf); [Mr Bean phone](https://tenor.com/view/mr-bean-rowan-atkinson-phone-call-hello-who-is-it-gif-18020495). No full visual yet.
- Rejected: registration-language meme contains disputed login/registration equivalence; tiny full-page forms unreadable on small card; school-enrolment illustration of uncertain AI origin not used. Generic salutation table is accurate but not a memorable visual.
- Candidates discovered: none ready yet. `26-base`, `27-base`, `28-base` are provisional gaps pending stronger search.
- Access failures: shell DNS blocked without escalation; escalated urllib request to Tenor succeeded. Existing assets can be downloaded with approved network access.
- Next action: actual clicking GIF, distinct outgoing call scene, and clean application document if mnemonic quality justifies it.

### Search S103 — 2026-10-25

- Card IDs: `29-base`, `30-base`, `31-base`, `34-base`.
- Search tool/site: web search.
- Exact queries: `site.tenor.com telephone dialing mr bean gif`; `site.tenor.com phone call hello gif`; `site.tenor.com answering machine friends joey`; `site.tenor.com answer question hermione hand`.
- Results: [Jonas Brothers answering phone](https://tenor.com/view/answering-phone-hello-hi-on-the-phone-overwhelmed-gif-15871652), official-partner uploader; [Friends answering machine](https://clip.cafe/friends-1994/i-got-machine-her-answering-machine/), video not a GIF; [Hermione discussion](https://time.com/5769779/best-harry-potter-memes/), secondary context only.
- Rejected: long dialogue about answering machine has no visible machine and depends on audio, so unsuitable. Picking up a receiver is not outgoing calling and would blur anrufen/answering.
- Access failures: none in web search.
- Next action: inspect exact assets; noun call needs distinctive incoming-call scene, verb answer needs active response, not a raised hand alone.

### Search S104 — 2026-10-25

- Card IDs: `34-base`, `35-base`, `36-base`, `39-base`, `40-base`, `41-base`, `42-base`.
- Search tool/site: web/image search.
- Exact queries: web `site.tenor.com "answer" "Hermione"`; `site.tenor.com "42" "answer"`; `site.tenor.com "appetite" "eating"`; `site.imgflip.com advertisement shut up take my money`; image `Apfel apple funny face`; `arbeiten work peon warcraft`; `die Arbeit work meme German`.
- Pages opened: [Gutefrage work meme](https://www.gutefrage.net/umfrage/versteht-ihr-das-meme-1), [apple template](https://www.meme-arsenal.com/create/template/6977211). [Schwarzer Kaffee office chart](https://schwarzer-kaffee.com/100-prozent-auf-arbeit/) returned cache miss in web; direct JPEG downloaded successfully, page to inspect via urllib. Existing apple photograph and office chart fully inspected locally. Clicking cursor GIF first frame inspected, motion not yet checked.
- Candidates: `39-base-A` humorous googly-eyed apple (meaning-only fallback with Apfel/apple cognate cue); `42-base-A` existing German Office meme explicitly containing Arbeit, noun-specific work setting; `21-base-A` cursor clicks (klick/click cue), motion pending.
- Rejected: Warcraft static peon has no explicit German cue and could mean warrior instead of worker. Fry paying depicts buying rather than advertisement; not a valid Anzeige illustration.
- Access failures: Schwarzer Kaffee page web cache miss; Jonas phone page web cache miss; retry via urllib is useful because direct asset downloads work.
- Next action: clearer outgoing telephone call, appetite GIF, and answer-result distinction.

### Search S105 — 2026-10-25

- Card IDs: `29-base`, `30-base`, `35-base`, `36-base`, `40-base`.
- Exact web queries: `site.tenor.com appetite hungry cookie monster`; `site.tenor.com "Dialing" "phone"`; `site.tenor.com "answer" "forty two"`; `site.tenor.com "advertisement" "old spice"`.
- Pages/results: broad telephone collection, Cookie Monster encyclopedia, Old Spice secondary articles and historical ads. No ready candidate from snippets alone. First-party or attributable existing asset needed.
- Rejected: Old Spice scene without clear ad context could retrieve man/horse/smell, not advertisement. 42 alone could just retrieve number; needs visible answer caption. Generic cookie-eating may depict eating, not appetite; inspect expression first.
- Next action: target actual existing captions and individual GIF URLs.

### Search S106 — 2026-10-25

- Card IDs: `24-base`, `29-base`, `34-base`, `35-base`, `36-base`, `40-base`.
- Exact web queries: `"die Anzeige" Werbung lustig Meme`; `"antworten" "Meme" deutsch`; `"die Antwort" "42" meme`; `"Appetit" "Krümelmonster" gif`. Image queries: `cookie monster hungry gif appetite`; `rotary phone dialing funny gif`; `ankreuzen Kästchen X Stift`.
- Pages opened: [Rhein-Lahn-Kreis](https://www.rhein-lahn-kreis.de/aktuelles/2024/briefwahlen-fuer-europa-und-kommunalwahlen-2024-im-rhein-lahn-kreis-welcher-zettel-muss-in-welchen-umschlag/) — existing red pencil draws X in checkbox; [green rotary dialing](https://makeagif.com/gif/green-rotary-phone-dialing-2_OvuR) — attributed uploader devinrader, external YouTube source; [Cookie Monster collection](https://tenor.com/search/cookie-monster-eating-cookies-gifs) — real GIF assets, individual page still needed.
- Candidates: checkbox `24-base-A` planned; original physical pen/cross gives a direct Kreuz/cross cue; not humorous. Cookie scene pending inspection. Outgoing dialing scene is clear but bland, provisional fallback rejected unless no better useful image.
- Rejected: humorous classified ad full of incorrect slang teaches misleading German and has too much tiny text; not used for Anzeige. 42 sans text remains ambiguous with numbers.
- Access failures: none in opened sources.
- Next action: download checkbox, single official Cookie Monster GIF and inspect, examine explicit German Antwort title card as optional fallback.

### Search S107 — 2026-10-25

- Card IDs: `34-base`, `35-base`.
- Exact image queries: `42 die Antwort auf fast alles arte logo`; `antworten Frage Antwort meme Deutsch`.
- Results: [Talking Animals creator's ARTE 42 project](https://talking-animals.com/work/arte-42.html) offers existing graphic with DIE ANTWORT AUF fast ALLES and bilingual French caption. Creator page is preferable to IMDb/aggregator reposts. Source and full visual not yet opened.
- Candidates: possible `35-base-A`, pending inspection; noun result answer, distinct from verb answering.
- Rejected: generic question/answer memes have no clear German-word association; Hermione raising a hand can mean volunteering rather than actually answering.
- Next action: creator page open, graphic download; leave antworten a gap if action cannot be made specific.

### Inspection update S107a — 2026-10-25 (no new search)

- Opened [creator ARTE project](https://talking-animals.com/work/arte-42.html); credits: animation director Jost Althoff; client mobyDOK; © Arte 2021, 2022; style guide Sonja Rohleder and Jana Kritchever. Embedded Vimeo video is `781069183`. Existing Vimeo thumbnail (as surfaced by image search) downloaded as `35-base-A.webp`, fully inspected: 42 above existing German DIE ANTWORT AUF fast ALLES and French subtitle. No added text. Meaning-only fallback for viewers who know 42 as the answer; may instead recall a number or TV show. Not a sound mnemonic.
- Opened individual [Cookie Monster GIF](https://tenor.com/view/sesame-street-cookie-monster-eats-your-art-eating-muppet-crazy-eyes-gif-1461380403278441959), uploader RedOfficialArt, underlying Sesame Street; no reuse license found. Downloaded 6,178,895-byte GIF; resized preserving 75 frames and 3750 ms duration to 309×320, now 3,380,467 bytes. Actual sampled frames inspected: enthusiastic cookie chomp; blue fur/eyes remain clear. `40-base-A`, meaning-only appetite fallback with Appetit/appetite cognate cue.
- Opened individual [Mr Bean GIF](https://tenor.com/view/mr-bean-rowan-atkinson-phone-call-hello-who-is-it-gif-18020495), GifGari official-partner upload; Rowan Atkinson/Mr Bean, episode unknown; reuse license unknown. Original 8,272,564 bytes, 498×389; resized all 82 frames to 320×250, 4100 ms preserved, 5,343,616 bytes. Sampled frames show inspecting large mobile then talking on it. `30-base-A` meaning-only telephone-call fallback; outgoing/incoming direction ambiguous, so do not reuse for outgoing verb `anrufen`.
- `24-base-A` full red pencil cross photo inspected; source page is official district government publisher, displayed photo credit to check. Resized 1920×1280 original 813,299 bytes to 960×640 JPEG 108,718 bytes.
- `41-base-A` German work/money meme inspected full size, but REJECTED: image shows talking heads rather than work, joke requires multi-sentence German A1 learner may not know. Download retained only as rejected evidence, excluded from gallery recommendations. Prefer a gap for arbeiten, deliberately distinct from Office work-setting noun Arbeit.
- `21-base-A` 7 frames, 350 ms; sampled cursor frames show click rays shift. First frame and later frame visually inspected; browser runtime playback pending root gallery review.
- Offline playback of GIFs pending root browser check; sampled frames plus successful GIF decoder are not claimed as runtime playback proof.

### Search S108 — 2026-10-25

- Card IDs: `28-base`, `29-base`, `31-base`, `34-base`.
- Exact web queries: `site.commons.wikimedia.org "Anrufbeantworter"`; `"anrufen" "Dach" "Hund"`; `"antworten" "Ant" mnemonic`. Exact image queries: `answering machine tape recorder telephone`; `die Anrede Herr Frau witz`.
- Opened: [Commons answering-machine symbol](https://commons.wikimedia.org/wiki/File:Symbol_Anrufbeantworter.svg), creator Josef Rosner; file description and licensing inspected; generic symbol not downloaded. Search results also showed telephone/answering machine product photographs and [DGPT museum article](https://dgpt.org/dinge-die-aus-unserem-alltag-nicht-so-ganz-verschwinden-der-anrufbeantworter/) (not opened, no visual inspection).
- Rejected: generic answering-machine icon is neither memorable nor a German-to-English connection; product photographs might mean telephone or tape recorder. Anrede cartoon uses Frauchen/Herrchen and animals, teaching different words from the target. Roof/dog calling and ant-answer proposals found no usable existing scenes; no invented explanation used.
- Candidates: none; gaps retained for Anrede, anrufen, Anrufbeantworter, antworten. A gap means no strong inspected option from these searches, not proof that no image exists.
- Access failures: none in this batch.
- Next useful search: first-party German-captioned outgoing-call cartoon, active answer scene with visible response, compact accurate registration comic, or user-provided familiar scene.

### Source follow-up S108a — 2026-10-25 (no new queries)

- Opened [All About Berlin registration form](https://allaboutberlin.com/docs/anmeldung) and [Duden anmelden](https://www.duden.de/rechtschreibung/anmelden) to check that login screenshots would not substitute a different meaning. Duden's registration/enrolment examples fit target, but generic login screenshots do not retrieve the requested sense. Keep `26-base`, `27-base` as separate gaps: verb needs registering action, noun needs application/registration result. Dense full-page forms are not recommended.
- Checked government source for pencil photo: no creator/license credit recovered in text; record unknown rather than assuming free use.
- Cropped `35-base-A.webp` from 1920×1080 at (590,280,1530,900) to 940×620 (78,364 bytes), keeping entire 42 and both existing German/French captions; no new text. Crop improves small-screen legibility. Original title frame attribution remains creator page / embedded Vimeo video.


### Review S009 — 2026-10-25 (no new search)

- Rejected `19-base-A`: all sampled frames of the full 14-frame GIF show Bugs Bunny dancing at the line, without starting. The actual asset contradicted the initial search suggestion. Retained as rejected evidence, never a gallery recommendation.
- `41-base-A` rejected by researcher: complex work/money dialogue over talking heads, no strong visual work connection. Excluded from gallery. Related noun Arbeit has its own explicit workplace caption; verb arbeiten stays a gap.
- The initial batch JSON included the rejected `41-base-A` within its card's candidate list; canonical manifest removes it from selectable candidates and retains it under rejected_candidates. `research-part-a.json`, `research-part-b.json`, download-list.json and the part-B Markdown are archival batch evidence, not assignment authorities. Resolve future choices against canonical manifest.
- Rendered and inspected desktop and mobile screenshots. Cropped `14-base-A` after mobile review from resized1200×882 at (370,35,1160,590) to790×555: exact IM ALTER caption and whole hippo/walker retained, extraneous birthday wishes/blank space removed. Before-crop copy retained only as evidence. No new text, illustrations or animation.
- Reran offline Chrome validation after crop/optional-label change: all 30 entries in exact order and exact German/English,16 images visible,4 GIFs animate,14 gaps; review/filter controls pass. GIFs:6-base-A(5frames),21-base-A(7),30-base-A(82),40-base-A(75). Gallery uses real local GIFs, not frame replacements.
- First browser launch in sandbox aborted; same isolated headless launch with approved escalation succeeded. No browser profile, personal Anki collection or study files accessed for image changes.
- Supporting screenshots: `anki/a1.1/image-candidates/review-desktop.png`, `review-mobile.png`. Verification script inspects current assets, sizes, hashes, frames, card order and preserved baseline, not only filenames.
- Source and direct-asset HTTP follow-up saved in source-link-checks.json. Page access checks supplement visual/source inspection; successful HTTP alone is not approval or proof of license. Any failing/redirecting links remain described in that report.

### Source repair S010 — 2026-10-25

- Card: `11-base`, same candidate `11-base-A` and same German poster, improved provenance.
- Link follow-up found old cinema page404 despite web cached page opening. Direct original asset200. New exact queries: `site.thalia-potsdam.de "Kevin" "Allein"`; `site.disney.de "Kevin" "Allein" poster`.
- IMDb media page returned403; not used. Opened working https://www.filmposter-archiv.de/filmplakat.php?id=3757 (web and urllib200), downloaded and visually inspected https://www.filmposter-archiv.de/filmplakat/1990/kevin_allein_zu_haus.jpg (492×700,100552bytes). Same German poster/title, no transformations. Gallery now links working source and asset; old download retained only as history. Official Disney+ source corroborates German title and alone plot.
- Other15 candidate source pages and all original direct assets returned200 in source-link-checks.json. This verifies access, not licensing. No study changes.

## Candidate records

All 16 retained candidates below were approved by the user on 26 October 2026 and integrated. Earlier search-log statuses describe the historical research state; current per-card decisions and validation live in canonical manifest. Source pages/full visuals were inspected; browser and installed Anki GIF playback and isolated reimport are now verified.

### Candidate 6-base-A — Pickup at school

- Card ID / exact German / exact English: `6-base` / abholen / to pick up / collect.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://tenor.com/view/mean-girls-shopping-gif-23164018
- Direct asset URL: https://media1.tenor.com/m/IF4OlkPc6rAAAAAC/mean-girls.gif
- Creator / film / scene attribution: Mean Girls (2004), Paramount; Tenor uploader blupanderz.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: animated GIF; GIF; 498×244 px; 408347 bytes; 5 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/6-base-A.gif`.
- Transformations: Unmodified download.
- Inspection: source page opened and full visual inspected; sampled frames inspected and animation verified offline in headless Chrome. Relevant metadata/hash in manifest.
- Memory connection: The car has arrived to collect someone: the existing invitation makes the pickup scene easy to remember.
- Match type: meaning-only fallback.
- Quality: Recommended for review; clear meaning, weaker German retrieval
- Ambiguities: Does not encode abholen by sound; shopping is incidental. Covers collecting a person rather than every kind of collection.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#6-base-A` / `manifest.json → cards → 6-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. GIF visibly animates offline in gallery/preview and in installed Anki 25.02.5 AnkiWebView, isolated profile.

- Packaged media filename: `a11_visual_6-base-A.gif`; approved asset SHA256 `844c0099e5a5dc28e2bcbe0551eacb03a2261b48d404601471842ef7bdaefdb6`.

### Candidate 8-base-A — Watch out for ducks

- Card ID / exact German / exact English: `8-base` / Achtung! / attention! / watch out!.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://schildbruder.de/produkt/schilder/schild-achtung-enten/
- Direct asset URL: https://schildbruder.de/storage/2024/11/10000621_Achtung_Enten.jpg
- Creator / film / scene attribution: Schildbruder retailer; individual designer unknown.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 800×800 px; 70923 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/8-base-A.jpg`.
- Transformations: Unmodified download.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: The exact German Achtung appears above a warning triangle containing an unexpectedly important duck: Achtung → watch out!
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: Enten is extra vocabulary inside the original asset; warning is more concrete than attention in general.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#8-base-A` / `manifest.json → cards → 8-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_8-base-A.jpg`; approved asset SHA256 `57c6cbdf1c3f7cbd6375b3e43b508f7a427a03a2d24d68bc281ebbc22974d17b`.

### Candidate 9-base-A — Harry Potter’s very specific address

- Card ID / exact German / exact English: `9-base` / die Adresse, Adressen / address.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://propstore.com/product/harry-potter-and-the-philosophers-stone-2001/lot-164-hero-wax-sealed-hogwarts-acceptance-letter/
- Direct asset URL: https://images.propstore.com/1d74eeab7c4845493d3291ac187692ea-1.jpg
- Creator / film / scene attribution: Harry Potter and the Philosopher’s Stone (2001); Propstore prop photograph; photographer unknown.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 734×734 px; 35754 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/9-base-A.jpg`.
- Transformations: Unmodified download.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: Adresse resembles address; Harry’s unusually precise cupboard address turns that familiar spelling into a memorable delivered letter.
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: Cognate-plus-scene aid, not a pronunciation guide. Shows a postal address rather than an email address. No new label is added.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#9-base-A` / `manifest.json → cards → 9-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_9-base-A.jpg`; approved asset SHA256 `54a2084641cf0845cc3d7771e85a9c61a989c4b761aa3b78f1751607d764df03`.

### Candidate 10-base-A — Clean ALL the things

- Card ID / exact German / exact English: `10-base` / alle / alles / all (everything).
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html
- Direct asset URL: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAbkmgiCg8x5ke0znAonSXIEicqHWfrw2N8JF1Ed4je44SdI7e0dnr2v1QNEpx8HkxeCRktVO21ymFhtSOM3ixyloG9l1bZvFDtwr7-XNyLo4V7Jo62DRHqqCM3mFSERC0XSdM47A-zB0/s400/responsibility12(alternate).png
- Creator / film / scene attribution: Allie Brosh, Hyperbole and a Half, This is Why I’ll Never be an Adult (2010).
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; PNG; 400×300 px; 33977 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/10-base-A.png`.
- Transformations: Unmodified download.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: Alle / alles begins like English all; the cartoon’s emphatic ALL THE THINGS anchors the everything meaning with comic overenthusiasm.
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: English spelling association only, not exact German pronunciation. Cleaning is the scene, not the word being learned.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#10-base-A` / `manifest.json → cards → 10-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_10-base-A.png`; approved asset SHA256 `9615b4a5133fb67fb1f82d22c6af1c058a30445faa370ee8fea4219dfbe73157`.

### Candidate 11-base-A — Kevin – Allein zu Haus

- Card ID / exact German / exact English: `11-base` / allein / alone.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.filmposter-archiv.de/filmplakat.php?id=3757
- Direct asset URL: https://www.filmposter-archiv.de/filmplakat/1990/kevin_allein_zu_haus.jpg
- Creator / film / scene attribution: Home Alone (1990), German theatrical poster, Filmposter-Archiv; title and plot corroborated by official Disney+.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 492×700 px; 100552 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/11-base-A-archive.jpg`.
- Transformations: Unmodified archive download of same German poster; prior cinema source page returned404..
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: The existing German title puts allein on the familiar Home Alone poster: alone is Kevin’s entire predicament.
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: Works best if you recognize Home Alone. Two burglars also appear; the plot/title, not a head count, carries alone. Small credits are incidental.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#11-base-A` / `manifest.json → cards → 11-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_11-base-A.jpg`; approved asset SHA256 `791d7c3ff9c05cd0eef6008b3c5b46d4cad5f1e2f5ca1cca2cbc92eae9cbb28a`.

### Candidate 13-base-A — Carl from Up

- Card ID / exact German / exact English: `13-base` / alt / old.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.pixar.com/upfilm
- Direct asset URL: https://images.squarespace-cdn.com/content/v1/60241cb68df65b530cd84d95/524984ff-b5da-44fd-a9b3-9f420c23bf87/carl15.jpg
- Creator / film / scene attribution: Disney/Pixar, Carl Fredricksen in Up (2009), official character image.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 1200×674 px; 87357 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/13-base-A.jpg`.
- Transformations: Resized only, max 1200px; aspect ratio, scene and text preserved.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: Carl’s gray hair, wrinkles and oversized glasses make an expressive, recognizable old character.
- Match type: meaning-only fallback.
- Quality: Recommended for review; clear meaning, weaker German retrieval
- Ambiguities: No German sound cue. Describes an old person; alt also describes old objects. Distinct from the Alter card’s noun caption about old age.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#13-base-A` / `manifest.json → cards → 13-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_13-base-A.jpg`; approved asset SHA256 `7dc573e1dde4322578c2a3b1dd08385d592cbd6622e6e6c8fae93c726ace7e71`.

### Candidate 14-base-A — Old age, hippo style

- Card ID / exact German / exact English: `14-base` / das Alter / age, old age.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.kartenparadies.at/products/geburtstag-lass-es-mal-richtig-krachen
- Direct asset URL: https://www.kartenparadies.at/cdn/shop/products/F-A-10innen.jpg?v=1619864324
- Creator / film / scene attribution: Edition Basic Funny-live series, retailer Kartenparadies; individual illustrator unknown.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 790×555 px; 97372 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/14-base-A.jpg`.
- Transformations: Resized whole original to 1200×882, then cropped (370,35,1160,590) to 790×555. Keeps IM ALTER caption and whole hippo/walker; removes blank space and unrelated birthday wishes. No added text..
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: The existing caption IM ALTER sits over a hippo with a walking frame making engine noises: old age gets a comic scene and the exact noun.
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: Extra German remains inside the original image. Old age is explicit in IM ALTER; unlike alt’s descriptive portrait. Cropped to improve small-screen caption legibility.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#14-base-A` / `manifest.json → cards → 14-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_14-base-A.jpg`; approved asset SHA256 `347c3e4091f0b37d5d7f2455161af8539275ee157e23f1a72769180d3effe9b3`.

### Candidate 17-base-A — An offer you can’t refuse

- Card ID / exact German / exact English: `17-base` / das Angebot, Angebote / offer.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.meme-arsenal.com/en/create/meme/3355963
- Direct asset URL: https://images.meme-arsenal.com/cbcb0abd2c9b59961b2a651736410fa8.jpg
- Creator / film / scene attribution: Marlon Brando / Don Vito Corleone, The Godfather (1972); meme author unknown; hosted by Meme-arsenal.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 600×449 px; 64744 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/17-base-A.jpg`.
- Transformations: Unmodified download.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: The familiar Godfather offer scene already contains Angebot in its German caption: the word leads to an unforgettable offer.
- Match type: German-word mnemonic.
- Quality: Recommended for review; direct German word/cognate connection
- Ambiguities: Assumes familiarity with the quotation. The threatening offer is an example, not the meaning of all offers. Existing caption remains intact.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#17-base-A` / `manifest.json → cards → 17-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_17-base-A.jpg`; approved asset SHA256 `d6abd166b25c5d3c698e2ea67d54375a9ccd3b438e15e152c8274985749641bb`.

### Candidate 20-base-A — The starting point

- Card ID / exact German / exact English: `20-base` / der Anfang / start.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.midliferun.today/blog/2017/7/21/cim-training-the-beginning-its-time-to-sweat-again
- Direct asset URL: https://images.squarespace-cdn.com/content/v1/5532ef55e4b06631eac2e194/1500696446556-KD7R4H6G6DRWRX5XIGBS/image-asset.jpeg
- Creator / film / scene attribution: Midlife Run blog photograph; photographer unknown.
- Usage or license information: Unknown; public viewing is not a reuse license. Original third-party content.
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 1200×801 px; 469539 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/20-base-A.jpg`.
- Transformations: Resized only, max 1200px; aspect ratio, scene and text preserved.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: A bare starting line identifies the noun start as a point/place, without showing someone starting an action.
- Match type: meaning-only fallback.
- Quality: Recommended for review; clear meaning, weaker German retrieval
- Ambiguities: Low humor and no German sound cue. Exact concrete meaning and excellent legibility; optional fallback rather than a top mnemonic. Physical start is narrower than a general beginning.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#20-base-A` / `manifest.json → cards → 20-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_20-base-A.jpg`; approved asset SHA256 `18ef05e9e4068c3d1fd5400b4e9700628459060bc2ea8b430717b2142fb9200a`.

### Candidate 21-base-A — Cursor click pulse

- Card ID / exact German / exact English: `21-base` / anklicken (etw. Akk.) / to click something.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://tenor.com/view/clicking-mouse-gif-25181352
- Direct asset URL: https://media1.tenor.com/m/x6BpJ7fthtIAAAAC/clicking-mouse.gif
- Creator / film / scene attribution: Tenor uploader Withersotrm120102; underlying animation creator unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: animated GIF; GIF; 498×498 px; 44345 bytes; 7 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/21-base-A.gif`.
- Transformations: none.
- Inspection: source page opened and full visual inspected; sampled frames inspected and animation verified offline in headless Chrome. Relevant metadata/hash in manifest.
- Memory connection: The visible pointer and click pulse attach the familiar klick/click cue in anklicken to clicking something. Motion distinguishes the click event from a static arrow.
- Match type: German-word mnemonic.
- Quality: Strong spelling/sound cue; simple high contrast at small sizes; low humor.
- Ambiguities: Pulse is very fast (350 ms); could resemble cursor movement without click context. Sound association is a memory aid, not pronunciation instruction.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#21-base-A` / `manifest.json → cards → 21-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. GIF visibly animates offline in gallery/preview and in installed Anki 25.02.5 AnkiWebView, isolated profile.

- Packaged media filename: `a11_visual_21-base-A.gif`; approved asset SHA256 `c8b30ff367b4caa6e297a4afc6a4f542bbe3cbf737f2e5c8dcdeb0a36bfd3bf7`.

### Candidate 24-base-A — Pencil marks a cross in a box

- Card ID / exact German / exact English: `24-base` / ankreuzen / to tick / mark with a cross.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.rhein-lahn-kreis.de/aktuelles/2024/briefwahlen-fuer-europa-und-kommunalwahlen-2024-im-rhein-lahn-kreis-welcher-zettel-muss-in-welchen-umschlag/
- Direct asset URL: https://www.rhein-lahn-kreis.de/rhein-lahn-kreis/politik-und-gremien/pen-2181101-1920.jpg?cid=68b.t0d
- Creator / film / scene attribution: Rhein-Lahn-Kreis source publisher; photographer unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 960×640 px; 108718 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/24-base-A.jpg`.
- Transformations: Resized 1920×1280 JPEG (813299 bytes) to 960×640 JPEG, quality90; whole scene retained..
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: Kreuz means cross: the pencil actively puts a red cross in a checkbox, tying kreuz in ankreuzen to marking/ticking a box.
- Match type: German-word mnemonic.
- Quality: Very clear action/object and generous close-up; direct word-part connection; no humor.
- Ambiguities: X is the relevant mark, not a mathematical multiplication or religious cross; photo does not show a tick-shaped checkmark.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#24-base-A` / `manifest.json → cards → 24-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_24-base-A.jpg`; approved asset SHA256 `93103d9b7c1bd34856d574224e15d806177ec9b49a7b7d78200dc296773aebc1`.

### Candidate 30-base-A — Mr Bean and the oversized mobile call

- Card ID / exact German / exact English: `30-base` / der Anruf, Anrufe / telephone call.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://tenor.com/view/mr-bean-rowan-atkinson-phone-call-hello-who-is-it-gif-18020495
- Direct asset URL: https://media1.tenor.com/m/1_KLvk5nIBkAAAAC/mr-bean-rowan-atkinson.gif
- Creator / film / scene attribution: Mr Bean / Rowan Atkinson; Tenor official-partner uploader GifGari; episode and rights holder unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: animated GIF; GIF; 320×250 px; 5343616 bytes; 82 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/30-base-A.gif`.
- Transformations: Resized all82 frames from498×389 (8272564 bytes) to320×250; duration4100ms and loop preserved..
- Inspection: source page opened and full visual inspected; sampled frames inspected and animation verified offline in headless Chrome. Relevant metadata/hash in manifest.
- Memory connection: A recognizable comic telephone conversation anchors the noun telephone call. It has no credible German-word sound link; use as a meaning-only fallback.
- Match type: meaning-only fallback.
- Quality: Recognizable character and comically large mobile; animation reveals the phone moving to his ear; scene stays readable at320px.
- Ambiguities: Incoming versus outgoing call is unspecified. Could also suggest phone/device; do not reuse it as proof of outgoing action anrufen. Existing GifGari watermark retained.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#30-base-A` / `manifest.json → cards → 30-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. GIF visibly animates offline in gallery/preview and in installed Anki 25.02.5 AnkiWebView, isolated profile.

- Packaged media filename: `a11_visual_30-base-A.gif`; approved asset SHA256 `bd483861584db45cb99af9137453f2c1e3590035b88930ae926a0eac19c5a625`.

### Candidate 35-base-A — 42 — Die Antwort auf fast alles

- Card ID / exact German / exact English: `35-base` / die Antwort, Antworten / answer.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://talking-animals.com/work/arte-42.html
- Direct asset URL: https://i.vimeocdn.com/video/1567837072-46964d97bbfd701a20f17972be34b49b2d093e6ce1ee18498a6e5efe7ea764ef-d?f=webp
- Creator / film / scene attribution: Talking Animals project: animation director Jost Althoff; client mobyDOK; ©Arte2021,2022; source page embeds Vimeo781069183. Style guide Sonja Rohleder and Jana Kritchever..
- Usage or license information: ©Arte2021,2022 per creator page; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: static image; WEBP; 940×620 px; 78364 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/35-base-A.webp`.
- Transformations: Cropped existing1920×1080 Vimeo thumbnail to(590,280,1530,900),940×620 WebP; entire42 and both existing German/French captions retained..
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: If 42 already recalls the famous answer joke, this existing title binds the written noun ANTWORT to that answer/result. It does not depict someone answering; deliberately distinct from verb antworten.
- Match type: meaning-only fallback.
- Quality: Existing word ANTWORT is prominent in cropped high-contrast title; useful only if42 is already a familiar answer reference.
- Ambiguities: Conditional usefulness: unfamiliar viewers may retrieve number42 or TV series rather than answer. French caption remains. No sound mnemonic and no new explanatory text in image.
- Recommendation / rejection reason: Optional conditional fallback; choose only if the 42 reference is familiar.
- Gallery reference / manifest reference: `index.html#35-base-A` / `manifest.json → cards → 35-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_35-base-A.webp`; approved asset SHA256 `18b2cd7be46e23a9b95a41d5ba9b396e6def6a4ce040d1522114d114b192836d`.

### Candidate 39-base-A — Googly-eyed wrinkled apple

- Card ID / exact German / exact English: `39-base` / der Apfel, Äpfel / apple.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://www.meme-arsenal.com/create/template/6977211
- Direct asset URL: https://images.meme-arsenal.com/e5e190ac018aae44ce79be995fac2a17.jpg
- Creator / film / scene attribution: Meme-Arsenal existing template6977211; photographer/creator unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 620×520 px; 44364 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/39-base-A.jpg`.
- Transformations: none.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: Apfel resembles apple in spelling and sound; the unmistakable apple with googly eyes gives that cognate a funny concrete face.
- Match type: German-word mnemonic.
- Quality: Recognizable fruit and unexpected face; readable without text at small size; strong cognate cue.
- Ambiguities: Wrinkled center may also suggest an old/rotten apple; no claim about etymology or exact pronunciation.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#39-base-A` / `manifest.json → cards → 39-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_39-base-A.jpg`; approved asset SHA256 `fe81878443224d70e174b2835a8b825b580171617d66092a137a5c2f01d27c69`.

### Candidate 40-base-A — Cookie Monster devours a cookie

- Card ID / exact German / exact English: `40-base` / der Appetit / appetite.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://tenor.com/view/sesame-street-cookie-monster-eats-your-art-eating-muppet-crazy-eyes-gif-1461380403278441959
- Direct asset URL: https://media1.tenor.com/m/FEfdu-sg7ecAAAAC/sesame-street-cookie-monster-eats-your-art.gif
- Creator / film / scene attribution: Sesame Street Cookie Monster; Tenor uploader RedOfficialArt; exact episode unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: animated GIF; GIF; 309×320 px; 3380467 bytes; 75 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/40-base-A.gif`.
- Transformations: Resized all75 frames from481×498 (6178895 bytes) to309×320;3750ms and loop preserved..
- Inspection: source page opened and full visual inspected; sampled frames inspected and animation verified offline in headless Chrome. Relevant metadata/hash in manifest.
- Memory connection: Appetit is close to appetite; Cookie Monster excitedly devouring the cookie supplies a memorable appetite/desire-for-food scene to anchor that cognate. The scene alone depicts meaning.
- Match type: German-word mnemonic.
- Quality: Appetit/appetite cognate is direct; eager expression and vigorous chomp are funny and clear without captions.
- Ambiguities: Could retrieve eating or hunger rather than appetite. The connection relies partly on the cognate, and does not imply correct German pronunciation from English.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#40-base-A` / `manifest.json → cards → 40-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. GIF visibly animates offline in gallery/preview and in installed Anki 25.02.5 AnkiWebView, isolated profile.

- Packaged media filename: `a11_visual_40-base-A.gif`; approved asset SHA256 `041a32ea7a22cd71baa7ea7a69285b33fe9480f074d599dcca7d37cadf3f6dc3`.

### Candidate 42-base-A — The Office — 100% auf der Arbeit

- Card ID / exact German / exact English: `42-base` / die Arbeit, Arbeiten / work.
- Status: integrated; user approved all 16 proposals on 26 October 2026.
- Source-page URL: https://schwarzer-kaffee.com/100-prozent-auf-arbeit/
- Direct asset URL: https://schwarzer-kaffee.com/bilder/2023/07/IMG-20230724-WA0000.jpg
- Creator / film / scene attribution: The Office Jim Halpert / John Krasinski scene; existing German meme published Schwarzer Kaffee; caption creator unknown.
- Usage or license information: unknown; no reuse license verified
- Accessed on: 2026-10-25.
- Asset: static image; JPEG; 720×801 px; 55400 bytes; 1 frame(s).
- Local path: `anki/a1.1/image-candidates/assets/42-base-A.jpg`.
- Transformations: none.
- Inspection: source page opened and full visual inspected; static asset decoded and visible offline in Chrome. Relevant metadata/hash in manifest.
- Memory connection: The existing caption explicitly pairs Arbeit with the office workplace. The joke distributes100% effort across the week, making work as a noun concrete and different from a verb action.
- Match type: German-word mnemonic.
- Quality: Visible Arbeit in a recognizable workplace and surprising percentage joke; main phrase readable in small preview.
- Ambiguities: Requires some German reading; lower percentage list may need full-size view on phone. No sound association; could evoke office or weekdays as well as work.
- Recommendation / rejection reason: Retained for user review based on the connection/clarity above; stronger direct-word cues take priority over fallbacks.
- Gallery reference / manifest reference: `index.html#42-base-A` / `manifest.json → cards → 42-base`.
- User decision:2026-10-26 exact message **“approve all”**; applies to this candidate and all 15 other proposed candidates.
- Integration checks: Packaged exact approved SHA256 bytes; correct Deck 01 answer/preview assignment; survives preparation and rebuilding; reimport preserves IDs/scheduling in isolated Anki 25.02.5 and 26.9.3. Offline image rendering checked in browser using actual Anki-rendered answer.

- Packaged media filename: `a11_visual_42-base-A.jpg`; approved asset SHA256 `a7a1346ef54aa439397b4a4041c609b00a2049a8e8ef8f80c742eaa1909a7e40`.

### Rejected candidates retained as evidence

- `19-base-A`: `assets/19-base-A.gif`; source https://tenor.com/view/start-bugs-bunny-ready-start-run-gif-13506050; direct URL in download-list.json; 14-frame 498×360 GIF. Full frames inspected, dancing rather than starting; rejected in S009. Never selected. See S008 for failed web fetch/direct HTML success.
- `41-base-A`: `assets/41-base-A.jpg`; details and original evidence in part-B report/manifest rejected_candidates. Complex dialogue and static talking heads weakly encode work; agent rejection, not a user decision. No integration.

## Approval — 2026-10-26

- Exact user message: **"approve all"**. Approved all 16 proposed candidates in canonical gallery/manifest. Four GIFs included.14 gaps remain; rejected19-base-A and 41-base-A are excluded.
- Recorded each selected_candidate_id and assignments_approved in canonical manifest before integration. Source assets retain approved SHA256 hashes.
- Captured original real package, actual9-field model, all 528 note GUIDs/field values, card deck/due data, and 525 MP3 hashes in validation/.
- Phase2 now in progress; no personal Anki collection is used.

## Phase2 integration evidence —2026-10-26

- Exact approval **“approve all”** recorded before any image assignment or rebuild. Integrated 6-base-A,8-base-A,9-base-A,10-base-A,11-base-A,13-base-A,14-base-A,17-base-A,20-base-A,21-base-A,24-base-A,30-base-A,35-base-A,39-base-A,40-base-A,42-base-A; 14 other Deck 01 cards remain gaps.
- Real original package backed up and schema/fields/GUIDs/tags/cards/media hashes captured before modification. Actual model 1792936801, unchanged 9-field order: ID,Headword,Details,English,Audio,OriginalGerman,OriginalEnglish,SpokenGerman,SourceID. No Image field added. Appended only `<div class="visual"><img src="..." alt=""></div>` to English on selected notes; original meaning text exact. Front/back templates unchanged. Original vocabulary cards.json and audio-manifest.json hash unchanged after prepare.
- Builder approval resolver permits only exact approved SHA256 assets for Deck 01; copies all 16 locally and packages only 525 MP3s+16 approved images. Preview embeds data URLs, including actual GIFs. No regeneration or new captions. Prototype .visual rendering rules reused;420px max image height improves readability without changing proportions.
- Two prepare/build/verify cycles passed; exact assignments persist outside cards.json. Original528 fields/meanings/order/repeats/GUIDs/deck IDs/tags and 525 audio byte hashes match real pre-image package. All 16 approved image hashes match package bytes. No images in Decks 02–18 or gaps.
- Verifier negative mutation tests rejected an image in Deck 02, image in a gap, wrong assignment, modified MP3 bytes, and autoplay; manifest resolver rejected an other-deck assignment. These used temporary mutated packages, never the deliverable.
- Default-import upgrade and repeat-import tested on Anki 25.02.5 (installed app version) and 26.9.3 backend, each in temporary collections.528 notes/cards, no duplicates; internal note/card IDs and simulated reviewed/lapsed/suspended scheduler columns exactly retained. Existing9-field schema and actual rendered image answers checked. Default import options suffice; no note-type merge needed.
- Chrome with external networking disabled checked all 528 preview entries and all 16 actual Anki-rendered package answers, exact front/details/meaning, local image loading, no JS errors, click-only actual MP3 playback and390px overflow. All4 GIFs visibly animate in gallery, preview and package answers. Visual screenshots inspected.
- Installed Anki 25.02.5 launched only with a purpose-built `/tmp/a11-anki-client-*` base/profile. Imported528 notes and displayed actual card answers in AnkiWebView.6-base,21-base,30-base,40-base GIFs produced multiple distinct actual rendered raster frames; screenshots retained. No personal collection opened. First-run setup and an initial static canvas-based measurement required correcting the test harness; raster capture establishes actual motion. Startup update-dialog callback warned during shutdown after test evidence was saved; no task data loss.
- Source records/gallery updated to Integrated with exact approval, hashes, local packaged filenames and validation references. Remaining gaps are intentional; research rejection reasons retained. Reimport into personal customized note types and mobile clients remains unverified.
- Reports/scripts/screenshots: `anki/a1.1/validation/README.md`; package report `anki/a1.1/verification.json`. All package media work offline. Current package SHA256 recorded in verification.json and preservation/reimport/persistence reports.

## Decision history

- 2026-10-26: user said **“approve all”**; approved all 16 proposed candidates. Integrated all 16, preserved14 gaps. Isolated reimport, browser rendering/audio/GIF and actual AnkiWebView GIF playback passed.

- 2026-10-25: researched all 30 cards; retained16 proposals and14 gaps. No user selections received. All recommendations are provisional.
- 2026-10-25: rejected19-base-A after actual animation inspection; rejected41-base-A after full visual review. These are research rejections, not user choices.
- 2026-10-25: improved14-base-A crop for phone legibility; candidate ID unchanged.35-base-A remains an explicitly conditional optional fallback. No study-card assignments changed.

## Reusable findings and dead ends

- Direct urllib downloads work with approved network escalation. Default shell DNS fails. Web image/page clicks occasionally return Internal Error/cache miss even when original HTML and assets are retrievable (S003,S007,S008,S107a). Check actual source before declaring an asset unavailable.
- Original creators/retailers are preferable to uncredited reposts where found: Allie Brosh, Pixar, Talking Animals, Schildbruder, Propstore, official district source. Hosting on a public page does not establish a reuse license; unknown licenses remain unknown.
- Existing exact German text works better than strained phonetic stories: Achtung warning, Angebot quotation, allein film title, Alter/Arbeit captions. Familiar cognates can also support humorous visuals (alle/all, Apfel/apple, Appetit/appetite).
- Avoid login/enrolment confusion, volunteer/answer confusion, telephone/tape-recorder confusion, and still images that imply the wrong verb. Similar verb/noun cards may deliberately have one candidate and one gap.
- Generic metaphor and search thumbnails alone are not selection evidence. See each source batch for failed queries and rejected leads; gaps describe these actual searches, not proof that no possible visual exists.

## Next handoff

- Task implemented and validated;16 illustrated cards (4 GIFs),14 gaps in Deck 01,528 cards/18 subdecks overall. All approved candidates integrated; none awaiting approval/integration.
- Canonical state: `anki/a1.1/image-candidates/manifest.json`. Assets in adjacent `assets/`; only approved media filenames are bundled. Research batches/rejected assets are historical evidence.
- Deliverables: package/preview/gallery/verification at paths in Current handoff; reports/scripts/screenshots in validation/.
- Preserved original 9-field schema/model/GUID/deck conventions. `prepare()` rewrites vocabulary only; keep approvals in separate manifest. Do not copy the prototype's different field order/model.
- Remaining limits: learner personal collection and mobile clients not tested; local note-type customizations not tested. All available isolated package/reimport/browser/AnkiWebView checks passed.
- Future work requires user direction; no unresolved integration blocker remains.
