"""Prove the package verifier rejects relevant image/audio/identity regressions."""
import contextlib
import importlib.util
import io
import json
import sqlite3
import tempfile
import zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('a11_build', ROOT/'build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
original = build.PACKAGE
checks={}
with tempfile.TemporaryDirectory(prefix='a11-negative-') as temp:
    temp=Path(temp)
    for label,position,change in [
        ('image_in_deck02',31,lambda fields: fields.__setitem__(3, fields[3]+'<img src="a11_visual_8-base-A.jpg">')),
        ('image_in_intentional_gap',1,lambda fields: fields.__setitem__(3, fields[3]+'<img src="a11_visual_8-base-A.jpg">')),
        ('wrong_approved_assignment',3,lambda fields: fields.__setitem__(3,fields[3].replace('a11_visual_6-base-A.gif','a11_visual_8-base-A.jpg'))),
        ('audio_autoplay',3,lambda fields: fields.__setitem__(4,fields[4].replace('<audio ','<audio autoplay '))),
    ]:
        database=temp/'collection.anki2'
        with zipfile.ZipFile(original) as z:
            database.write_bytes(z.read('collection.anki2'))
            with sqlite3.connect(database) as db:
                nid,flds=db.execute('select n.id,n.flds from notes n join cards c on n.id=c.nid where c.due=?',(position,)).fetchone()
                fields=flds.split('\x1f');change(fields)
                db.execute('update notes set flds=? where id=?',('\x1f'.join(fields),nid))
            package=temp/f'{label}.apkg'
            with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as out:
                for name in z.namelist():out.writestr(name,database.read_bytes() if name=='collection.anki2' else z.read(name))
        build.PACKAGE=package
        try:
            with contextlib.redirect_stdout(io.StringIO()):build.verify()
        except AssertionError:checks[label]='rejected'
        else:raise AssertionError(f'Verifier accepted {label}')
    # Tamper a bundled MP3 while retaining length and valid archive.
    with zipfile.ZipFile(original) as z,zipfile.ZipFile(temp/'audio-change.apkg','w',zipfile.ZIP_DEFLATED) as out:
        mapping=json.loads(z.read('media'));key=next(k for k,n in mapping.items() if n.endswith('.mp3'))
        for name in z.namelist():
            data=z.read(name)
            if name==key:data=data[:-1]+bytes([data[-1]^1])
            out.writestr(name,data)
    build.PACKAGE=temp/'audio-change.apkg'
    try:build.verify()
    except AssertionError:checks['changed_mp3_bytes']='rejected'
    else:raise AssertionError('Verifier accepted changed audio')
    # A proposed assignment into another subdeck must fail before packaging.
    cards=build.load_cards();cards[2]['deck']=2
    try:build.approved_images(cards)
    except AssertionError:checks['manifest_assignment_outside_deck01']='rejected'
    else:raise AssertionError('Assignment outside Deck01 accepted')
    build.PACKAGE=original
(ROOT/'validation/verifier-negative-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
