"""Temporary add-on for an explicitly isolated Anki base; never install in personal profile."""
import hashlib
import json
import traceback
from pathlib import Path
from aqt import mw, gui_hooks
from aqt.qt import QTimer
from anki import import_export_pb2 as pb

ROOT = Path('/Users/muhammednasim/Desktop/a1/anki/a1.1')
REPORT = {'measurement':'QtWebView raster snapshots; canvas drawImage can use a static GIF frame', 'client':'installed Anki25.02.5 / AnkiWebView QtWebEngine','isolated_base':True,'personal_collection_accessed':False,'gifs':{}}
QUEUE = []
CURRENT = None
HASHES = []
ATTEMPTS = 0


def finish(error=None):
    if error:
        REPORT['error']=str(error)
    (ROOT/'validation/anki-client-verification.json').write_text(json.dumps(REPORT,indent=2)+'\n')
    QTimer.singleShot(100, mw.close)


def sample():
    js='''(()=>{const i=document.querySelector('img');return !!(i&&i.complete&&i.naturalWidth);})()'''
    mw.web.evalWithCallback(js, got_sample)


def got_sample(value):
    global ATTEMPTS
    try:
        ATTEMPTS+=1
        if value:
            image=mw.web.grab().toImage()
            HASHES.append(hashlib.sha256(image.bits().asstring(image.sizeInBytes())).hexdigest())
        if len(HASHES)<6 and ATTEMPTS<30:
            QTimer.singleShot(173,sample)
            return
        unique=len(set(HASHES))
        if unique<2:
            raise RuntimeError('GIF did not animate: '+CURRENT)
        REPORT['gifs'][CURRENT]={'visible':True,'distinct_rendered_frames':unique,'animated':True}
        mw.web.grab().save(str(ROOT/'validation'/('anki-'+CURRENT+'.png')))
        QTimer.singleShot(100,next_card)
    except Exception:
        finish(traceback.format_exc())


def next_card():
    global CURRENT,HASHES,ATTEMPTS
    try:
        if not QUEUE:
            REPORT['all_four_gifs_animate']=True
            return finish()
        cid,filename=QUEUE.pop(0)
        CURRENT=cid;HASHES=[];ATTEMPTS=0
        nid=mw.col.db.scalar('select id from notes where flds like ?',cid+'\x1f%')
        card=mw.col.get_note(nid).cards()[0]
        answer=card.answer()
        assert filename in answer
        mw.web.stdHtml(answer, context=mw.reviewer)
        QTimer.singleShot(800,sample)
    except Exception:
        finish(traceback.format_exc())


def run():
    try:
        # Refuse to run anywhere except this purpose-built disposable profile base.
        assert str(mw.pm.base).startswith('/tmp/a11-anki-client-') or str(mw.pm.base).startswith('/private/tmp/a11-anki-client-')
        request=pb.ImportAnkiPackageRequest(package_path=str(ROOT/'german-a1.1.apkg'),options=pb.ImportAnkiPackageOptions())
        mw.col.import_anki_package(request)
        assert mw.col.db.scalar('select count(*) from notes')==528
        m=json.loads((ROOT/'image-candidates/manifest.json').read_text())
        for cid,a in m['assignments_approved'].items():
            if m['cards'][cid]['candidates'][0]['frames']>1:QUEUE.append((cid,a['media_file']))
        assert len(QUEUE)==4
        REPORT['imported_notes']=528
        mw.resize(800,800)
        QTimer.singleShot(100,next_card)
    except Exception:
        finish(traceback.format_exc())


gui_hooks.profile_did_open.append(lambda: QTimer.singleShot(500,run))
QTimer.singleShot(60000,lambda:finish('Client test timed out') if not REPORT.get('all_four_gifs_animate') else None)
