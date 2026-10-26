"""Run only on disposable collections; old package then upgraded package then repeat."""
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from anki.collection import Collection
from anki import import_export_pb2 as pb
from importlib.metadata import version as package_version

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / 'image-candidates/manifest.json').read_text())
APPROVED = MANIFEST['assignments_approved']
REPORT = {'package_sha256': hashlib.sha256((ROOT / 'german-a1.1.apkg').read_bytes()).hexdigest(), 'anki_backend_version': package_version('anki'), 'personal_collection_accessed': False}


def do_import(col, path):
    request = pb.ImportAnkiPackageRequest(package_path=str(path), options=pb.ImportAnkiPackageOptions())
    return col.import_anki_package(request)


def card_state(col):
    # Include the internal note/card IDs and all scheduler columns, not only GUIDs.
    return col.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags from cards order by id')


with tempfile.TemporaryDirectory(prefix='a11-reimport-') as directory:
    col = Collection(str(Path(directory) / 'collection.anki2'))
    do_import(col, ROOT / 'validation/before-images.apkg')
    assert col.db.scalar('select count(*) from notes') == 528
    old_models = {x['id']: x for x in col.models.all()}
    # Simulate a learner with existing reviewed, lapsed and suspended cards.
    ids = col.db.list('select id from cards order by id limit 3')
    col.db.execute('update cards set type=2,queue=2,due=451,ivl=27,factor=2450,reps=12,lapses=2 where id=?', ids[0])
    col.db.execute('update cards set queue=-1 where id=?', ids[1])
    before = card_state(col)
    guids = col.db.all('select id,guid,mid from notes order by id')
    do_import(col, ROOT / 'german-a1.1.apkg')
    assert card_state(col) == before, 'Scheduling or internal card identity changed'
    assert col.db.all('select id,guid,mid from notes order by id') == guids
    assert col.db.scalar('select count(*) from notes') == 528
    assert col.db.scalar('select count(*) from cards') == 528
    model = col.models.get(1792936801)
    assert [f['name'] for f in model['flds']] == [f['name'] for f in old_models[1792936801]['flds']]
    illustrated = {}
    for nid in col.db.list('select id from notes'):
        note = col.get_note(nid)
        cid = note['ID']
        if cid in APPROVED:
            assert APPROVED[cid]['media_file'] in note['English'], f'Note did not update: {cid}'
            illustrated[cid] = APPROVED[cid]['candidate_id']
        else:
            assert '<img' not in note['English']
    assert len(illustrated) == 16
    assert col.db.scalar('select count(distinct did) from cards') == 18
    # Read Anki's actual rendered answer, not just package field HTML.
    rendered = {}
    for cid in APPROVED:
        nid = col.db.scalar('select id from notes where flds like ?', cid + '\x1f%')
        card = col.get_note(nid).cards()[0]
        answer = card.answer()
        assert APPROVED[cid]['media_file'] in answer
        rendered[cid] = {'question': card.question(), 'answer': answer}
    # Media were copied by Anki importer, including original animated files.
    media_dir = Path(col.media.dir())
    for cid, a in APPROVED.items():
        data = (media_dir / a['media_file']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == a['sha256']
    do_import(col, ROOT / 'german-a1.1.apkg')
    assert card_state(col) == before
    assert col.db.scalar('select count(*) from notes') == 528
    REPORT.update(initial_import_notes=528, upgraded_notes=528, duplicate_notes=0,
                  illustrated_cards=len(illustrated), subdecks=18, nine_field_schema_unchanged=True,
                  internal_note_and_card_ids_preserved=True, scheduling_preserved=True,
                  reviewed_and_suspended_examples_checked=True, repeat_import_idempotent=True,
                  approved_media_bytes_verified=True, import_options='Defaults; no note-type merge, no scheduling import')
    (ROOT / 'validation/rendered-anki-cards.json').write_text(json.dumps(rendered, ensure_ascii=False, indent=2)+'\n')
    col.close()
version = str(package_version('anki')).replace('.', '-')
(ROOT / f'validation/reimport-{version}.json').write_text(json.dumps(REPORT, indent=2)+'\n')
print(json.dumps(REPORT, indent=2))
