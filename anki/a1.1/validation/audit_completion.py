"""Audit current deliverables against approval, baseline, preview and test evidence."""
import base64
import hashlib
import json
import re
from pathlib import Path
from PIL import Image

R=Path(__file__).resolve().parent.parent
V=R/'validation'
def read(path):return json.loads(path.read_text())
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
manifest=read(R/'image-candidates/manifest.json')
assert manifest['approval']['exact_user_message']=='approve all'
assert len(manifest['cards'])==30 and len(manifest['assignments_approved'])==16
assert sum(c['status']=='Gap' for c in manifest['cards'].values())==14
assert all(c['status']=='Integrated' for c in manifest['cards'].values() if c['selected_candidate_id'])
cards=read(R/'cards.json');baseline=read(R/'image-candidates/baseline.json')
assert len(cards)==528 and digest(R/'cards.json')==baseline['files']['cards.json']
assert digest(R/'audio-manifest.json')==baseline['files']['audio-manifest.json']
assert [c['card_id'] for c in cards[:30]]==list(manifest['cards'])
package_hash=digest(R/'german-a1.1.apkg')
verification=read(R/'verification.json')
assert verification['package_sha256']==package_hash
assert (verification['cards'],verification['decks'],verification['images'],verification['animated_gifs'],verification['deck_01_image_gaps'])==(528,18,16,4,14)
for f in ['reimport-25-02-5.json','reimport-26-9-3.json','persistence.json']:
 assert read(V/f)['package_sha256']==package_hash
preserved=read(V/'preservation.json')
assert preserved['current_package_sha256']==package_hash and preserved['unchanged_audio_bytes']==525
assert all(v=='rejected' for v in read(V/'verifier-negative-checks.json').values())
text=(R/'preview.html').read_text()
match=re.search(r'const DATA = (\{.*\});\nconst byId',text)
assert match
preview=json.loads(match.group(1))
assert preview['cards']==cards
assert set(preview['images'])==set(manifest['assignments_approved'])
assert len(preview['audio'])==525
for name,data in preview['audio'].items():
 assert hashlib.sha256(base64.b64decode(data.split(',',1)[1])).hexdigest()==read(V/'baseline-content.json')['media_hashes'][name]
for cid,a in manifest['assignments_approved'].items():
 record=manifest['cards'][cid];candidate=record['candidates'][0]
 source=R/'image-candidates'/candidate['local_path']
 assert digest(source)==a['sha256']==digest(R/'media'/a['media_file'])
 assert hashlib.sha256(base64.b64decode(preview['images'][cid].split(',',1)[1])).hexdigest()==a['sha256']
 with Image.open(source) as im:
  assert list(im.size)==candidate['dimensions']
  assert getattr(im,'n_frames',1)==candidate['frames']
browser=read(V/'browser-verification.json')
assert browser['preview_cards_checked']==528 and browser['package_answers_checked']==16
assert browser['preview_audio_click_playback'] and browser['preview_no_autoplay_during_528_card_navigation']
assert browser['package_audio_click_playback'] and browser['mobile_no_horizontal_overflow']
assert not browser['javascript_errors']
assert len(browser['gif_playback'])==4
for test in browser['gif_playback'].values():assert all(v>1 for v in test.values())
client=read(V/'anki-client-verification.json')
assert client['all_four_gifs_animate'] and client['imported_notes']==528 and not client['personal_collection_accessed']
assert len(client['gifs'])==4 and all(x['animated'] and x['distinct_rendered_frames']>1 for x in client['gifs'].values())
research=(R.parents[1]/'docs/anki-deck-01-visual-research.md').read_text()
for cid,c in manifest['cards'].items():
 assert cid in research
 for a in c['candidates']:
  assert '### Candidate '+a['candidate_id'] in research
assert 'approve all' in research and '## Phase2 integration evidence' in research
for f in ['README.md','preview.html','german-a1.1.apkg','verification.json','image-candidates/index.html','image-candidates/manifest.json','validation/README.md']:
 assert (R/f).is_file()
report={'date':'2026-10-26','complete':True,'cards':528,'subdecks':18,'deck01_cards':30,'illustrated_cards':16,'animated_gifs':4,'intentional_deck01_gaps':14,'approved_only':True,'original_vocabulary_audio_and_ids_preserved':True,'preparation_persistence_verified':True,'offline_media_and_click_only_audio_verified':True,'reimport_verified_versions':['25.02.5','26.9.3'],'gif_animation_verified_in':['offline gallery','offline preview','Anki-rendered package answers in Chrome','installed Anki25.02.5 AnkiWebView, isolated profile'],'personal_collection_accessed':False,'limitations':['AnkiMobile/AnkiDroid and physical devices not tested.','Personal locally customized note types not tested.'],'artifact_sha256':{f:digest(R/f) for f in ['german-a1.1.apkg','preview.html','cards.json','audio-manifest.json','build.py','preview-template.html','image-candidates/manifest.json','image-candidates/index.html','verification.json']}}
(V/'completion-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
