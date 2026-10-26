"""Verify the actual offline preview, gallery, and Anki-rendered package answers."""
import asyncio
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
V = ROOT / 'validation'
M = json.loads((ROOT / 'image-candidates/manifest.json').read_text())
CARDS = json.loads((ROOT / 'cards.json').read_text())
REPORT = {'network': 'offline', 'client': 'isolated headless Google Chrome', 'preview_cards_checked': 0, 'package_answers_checked': 0, 'gif_playback': {}}


async def animated(locator):
    await locator.scroll_into_view_if_needed()
    hashes = []
    for _ in range(5):
        hashes.append(hashlib.sha256(await locator.screenshot()).hexdigest())
        await asyncio.sleep(.137)
    assert len(set(hashes)) > 1
    return len(set(hashes))


async def main():
    with tempfile.TemporaryDirectory(prefix='a11-render-') as temp:
        media = Path(temp)
        with zipfile.ZipFile(ROOT / 'german-a1.1.apkg') as z:
            for key, name in json.loads(z.read('media')).items():
                (media / name).write_bytes(z.read(key))
        rendered = json.loads((V / 'rendered-anki-cards.json').read_text())
        async with async_playwright() as p:
            browser = await p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless=True)
            context = await browser.new_context(offline=True, viewport={'width':390,'height':844})
            page = await context.new_page()
            errors=[]
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.add_init_script("window.audioPlays=0;document.addEventListener('play',()=>window.audioPlays++,true);")
            await page.goto((ROOT/'preview.html').as_uri())
            await page.wait_for_load_state('load')
            assert await page.evaluate('Object.keys(DATA.audio).length') == 525
            assert await page.evaluate('Object.keys(DATA.images).length') == 16
            for idx,card in enumerate(CARDS):
                await page.evaluate('(i)=>{index=i;render();}', idx)
                assert await page.locator('#english').inner_text() == card['english']
                assert await page.locator('#german').inner_text() == card['headword']
                assert await page.locator('#details').inner_text() == card['details']
                present = card['card_id'] in M['assignments_approved']
                assert await page.locator('#visual img').count() == int(present)
                if present:
                    await page.locator('#visual img').evaluate('(i)=>i.decode()')
                REPORT['preview_cards_checked'] += 1
            assert await page.evaluate('window.audioPlays') == 0
            await page.locator('#play').click()
            await page.wait_for_function('audio && !audio.paused && audio.readyState >= 2')
            assert await page.evaluate('Number.isFinite(audio.duration) && audio.duration>0')
            await page.evaluate('audio.pause()')
            REPORT['preview_audio_click_playback'] = True
            REPORT['preview_no_autoplay_during_528_card_navigation'] = True
            for cid,assignment in M['assignments_approved'].items():
                record = M['cards'][cid]
                await page.evaluate('(i)=>{index=i;render();}', record['position']-1)
                if record['candidates'][0]['frames'] > 1:
                    count = await animated(page.locator('#visual img'))
                    REPORT['gif_playback'].setdefault(assignment['candidate_id'],{})['preview_distinct_frames'] = count
            await page.evaluate('index=2;render();')
            await page.locator('#visual').scroll_into_view_if_needed()
            await page.screenshot(path=str(V/'preview-mobile.png'))
            assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            for cid,html in rendered.items():
                file=media/'card.html'
                file.write_text('<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><body class="card">'+html['answer']+'</body>')
                await page.goto(file.as_uri())
                img=page.locator('img')
                assert await img.count()==1
                await img.evaluate('(i)=>i.decode()')
                assert await page.locator('.meaning').inner_text()==next(c['english'] for c in CARDS if c['card_id']==cid)
                assert await page.locator('audio,button').count()==0
                assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                if M['cards'][cid]['candidates'][0]['frames']>1:
                    REPORT['gif_playback'][M['assignments_approved'][cid]['candidate_id']]['package_answer_distinct_frames']=await animated(img)
                REPORT['package_answers_checked']+=1
                if cid=='42-base':
                    await page.screenshot(path=str(V/'package-back-mobile.png'))
            # Exercise the actual package front's click handler using packaged MP3s.
            file.write_text('<!doctype html><body class="card">'+rendered['6-base']['question']+'</body>')
            await page.goto(file.as_uri())
            assert await page.evaluate('window.audioPlays')==0
            await page.locator('.pronounce').click()
            await page.wait_for_function('document.querySelector("audio").readyState>=2 && !document.querySelector("audio").paused')
            REPORT['package_audio_click_playback']=True
            await page.goto((ROOT/'image-candidates/index.html').as_uri())
            assert await page.locator('.entry').count()==30
            assert await page.locator('.preview img').count()==16
            for cid,a in M['assignments_approved'].items():
                img=page.locator('[id="'+a['candidate_id']+'"] img')
                await img.evaluate('(i)=>i.decode()')
                if M['cards'][cid]['candidates'][0]['frames']>1:
                    REPORT['gif_playback'][a['candidate_id']]['gallery_distinct_frames']=await animated(img)
            REPORT['gallery_all_16_images_visible']=True
            REPORT['mobile_no_horizontal_overflow']=True
            REPORT['javascript_errors']=errors
            assert not errors
            await page.set_viewport_size({'width':1280,'height':900})
            await page.goto((ROOT/'preview.html').as_uri())
            await page.evaluate('index=3;render();')
            await page.screenshot(path=str(V/'preview-desktop.png'))
            REPORT['desktop_layout_checked']=True
            await browser.close()
    (V/'browser-verification.json').write_text(json.dumps(REPORT,indent=2)+'\n')
    print(json.dumps(REPORT,indent=2))

asyncio.run(main())
