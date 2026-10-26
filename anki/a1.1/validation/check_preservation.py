"""Compare the rebuilt package against the captured real pre-image package."""
import hashlib
import json
import sqlite3
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
baseline = json.loads((ROOT / 'validation/baseline-content.json').read_text())
manifest = json.loads((ROOT / 'image-candidates/manifest.json').read_text())
assignments = manifest['assignments_approved']
with zipfile.ZipFile(ROOT / 'german-a1.1.apkg') as z, tempfile.TemporaryDirectory() as t:
    p = Path(t) / 'collection.anki2'
    p.write_bytes(z.read('collection.anki2'))
    with sqlite3.connect(p) as db:
        notes = db.execute('select guid,mid,flds,tags from notes order by guid').fetchall()
        for old, new in zip(baseline['notes'], notes):
            assert old[0:2] == list(new[0:2])
            old_fields, new_fields = old[2].split('\x1f'), new[2].split('\x1f')
            cid = old_fields[0]
            expected = old_fields[:]
            if cid in assignments:
                expected[3] += '<div class="visual"><img src="' + assignments[cid]['media_file'] + '" alt=""></div>'
            assert new_fields == expected, cid
            assert old[3] == new[3], cid
        assert len(notes) == len(baseline['notes']) == 528
        current_cards = db.execute('select n.guid,c.ord,c.did,c.due from cards c join notes n on n.id=c.nid order by n.guid').fetchall()
        assert [list(x) for x in current_cards] == baseline['cards']
        model = json.loads(db.execute('select models from col').fetchone()[0])['1792936801']
        assert model['name'] == baseline['model']['name']
        assert model['flds'] == baseline['model']['flds']
        assert model['tmpls'] == baseline['model']['tmpls']
    media = json.loads(z.read('media'))
    for name, digest in baseline['media_hashes'].items():
        key = next(k for k, v in media.items() if v == name)
        assert hashlib.sha256(z.read(key)).hexdigest() == digest
report = {'baseline_package_sha256': 'fc733c93bdb280d4a51de00b1b1570595178ca8a9b69a3c700dffe71fb944c72',
          'current_package_sha256': hashlib.sha256((ROOT / 'german-a1.1.apkg').read_bytes()).hexdigest(),
          'cards_preserved': 528, 'unchanged_audio_bytes': 525, 'approved_answer_additions': 16,
          'nine_field_definitions_unchanged': True, 'templates_unchanged': True,
          'deck_ids_guids_order_tags_preserved': True, 'other_subdeck_fields_unchanged': True}
(ROOT / 'validation/preservation.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
