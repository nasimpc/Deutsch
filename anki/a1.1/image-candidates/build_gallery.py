"""Render the offline research gallery; never writes study data or assignments."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def esc(value):
    return html.escape(str(value), quote=True)


def render():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    rows = []
    for card in manifest['cards'].values():
        candidates = []
        for c in card['candidates']:
            size = c['file_size_bytes'] / 1024
            candidates.append(f'''<article class="candidate" id="{esc(c['candidate_id'])}">
<div class="preview"><a href="{esc(c['local_path'])}" target="_blank" title="Open full-size asset"><img src="{esc(c['local_path'])}" alt="{esc(c['title'])}"></a></div>
<div class="detail"><p class="tag">{esc(c.get('recommendation', 'Recommended' if card['recommended_candidate_id'] == c['candidate_id'] else 'Alternative'))} · {esc(c['match_type'])}</p>
<h3>{esc(c['candidate_id'])} · {esc(c['title'])}</h3>
<p class="meta">{esc(c['asset_type'])} · {esc(c['format'])} · {' × '.join(map(str,c['dimensions']))} px · {size:.0f} KB{(' · '+str(c['frames'])+' frames') if c['frames']>1 else ''}</p>
<p>{esc(c['memory_connection'])}</p><p class="ambiguity"><b>Ambiguity:</b> {esc(c['ambiguities'])}</p>
<p class="meta">{esc(c['creator'])}<br>Usage: {esc(c['usage'])}</p>
<p><a href="{esc(c['source_page_url'])}" target="_blank" rel="noreferrer">Source page ↗</a> · <a href="{esc(c['image_url'])}" target="_blank" rel="noreferrer">Original asset ↗</a> · <a href="{esc(c['local_path'])}" target="_blank">Full size</a></p>
<p class="choice">{esc(c['status'].capitalize())} · {esc(c['candidate_id'])}</p></div></article>''')
        content = ''.join(candidates) if candidates else '<div class="gap"><b>Gap · no strong candidate</b><p>'+esc(card['gap_reason'])+'</p></div>'
        rows.append(f'''<section class="entry {'has-candidate' if candidates else 'is-gap'}" id="card-{esc(card['card_id'])}" data-card="{esc(card['card_id'])}"><div class="heading"><span class="number">{card['position']:02}</span><div><h2 lang="de">{esc(card['german'])}</h2><p class="translation">{esc(card['english'])}</p><p class="meta">Stable card ID: {esc(card['card_id'])} · {esc(card['status'])}</p></div></div>{content}</section>''')
    nav = ''.join(f'<a href="#card-{esc(c["card_id"])}" title="{esc(c["german"])}">{c["position"]:02}</a>' for c in manifest['cards'].values())
    ready=sum(bool(c['candidates']) for c in manifest['cards'].values())
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Deck 01 · Visual candidate review</title>
<style>*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#edf3fb;color:#16396c;font:16px/1.55 system-ui,-apple-system,sans-serif}main{max-width:1100px;margin:auto;padding:32px 20px 80px}h1{font-size:clamp(30px,5vw,48px);line-height:1.1;letter-spacing:-1.5px;margin:12px 0}h2{font-size:25px;margin:0;overflow-wrap:anywhere}h3{font-size:18px;margin:8px 0}p{margin:10px 0}a{color:#245edb;overflow-wrap:anywhere}header{margin-bottom:30px}.eyebrow,.tag{color:#245edb;font-weight:650;font-size:13px}.notice{background:#e1edff;border-left:4px solid #397ef0;padding:14px 18px;margin:20px 0;border-radius:8px}.meta{font-size:13px;color:#5e7391}.entry{border:1px solid #d2dff2;border-radius:20px;background:white;margin:20px 0;overflow:hidden;scroll-margin-top:20px}.heading{display:flex;align-items:flex-start;gap:16px;padding:22px}.number{font-size:15px;background:#e7f0ff;border-radius:10px;padding:8px 12px;color:#245edb;font-weight:700}.translation{margin:3px 0;font-size:18px}.heading .meta{margin:4px 0}.candidate{display:grid;grid-template-columns:minmax(230px,42%) 1fr;border-top:1px solid #e4ebf6}.preview{padding:20px;display:grid;place-items:center;background:#f7f9fd;min-width:0}.preview a{display:block;max-width:100%}.preview img{display:block;max-width:100%;max-height:420px;width:auto;height:auto;margin:auto;object-fit:contain}.detail{padding:18px 24px;min-width:0}.ambiguity{font-size:14px;color:#52647d}.gap{border-top:1px dashed #d2dff2;padding:18px 24px;color:#52647d;background:#fafcff}.gap p{margin-bottom:0}.choice{display:block;background:#edf4ff;padding:12px;border-radius:8px;font-size:14px}.choice input{width:18px;height:18px;vertical-align:middle;margin-right:8px}nav{display:flex;flex-wrap:wrap;gap:5px;margin:20px 0}nav a{padding:6px 9px;background:white;border-radius:6px;text-decoration:none;font-size:13px}.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:20px}button,select{font:inherit;font-size:14px;background:white;color:#245edb;border:1px solid #b9d2fa;border-radius:8px;padding:10px;cursor:pointer}textarea{display:block;width:100%;min-height:90px;margin-top:10px;border:1px solid #b9d2fa;border-radius:8px;padding:12px;font:14px/1.5 system-ui;color:#16396c}input:focus-visible,a:focus-visible,button:focus-visible,select:focus-visible{outline:3px solid #80afff;outline-offset:3px}[hidden]{display:none!important}@media(max-width:680px){main{padding:22px 12px 50px}.candidate{grid-template-columns:1fr}.preview img{max-height:450px}.detail{padding:16px 20px}.heading{padding:18px 16px;gap:12px}h2{font-size:22px}.preview{padding:16px}}</style>
<main><header><p class="eyebrow">GERMAN A1.1 / DECK 01 / RESEARCH REVIEW</p><h1>Words worth remembering.</h1>
<p>30 cards in their exact study order · READY cards with proposed visuals · GAPS intentional gaps</p>
<div class="notice"><b>Approval pending.</b> These visuals have not been added to your deck. Pick by candidate ID, or leave any entry without an image. German-word mnemonics rank above meaning-only fallbacks. Sound/spelling associations are memory aids; keep using the real German audio.</div>
<p class="meta">Existing assets only. Click a preview for full size. GIFs retain their animation. Explanations, credits and selection controls belong only to this research gallery. The study package and preview remain unchanged pending approval.</p>
<nav aria-label="Jump to card">NAV</nav><div class="toolbar"><label>Show <select id="filter"><option value="all">All 30 cards</option><option value="candidate">Cards with candidates</option><option value="gap">Gaps</option></select></label><button id="summarize">Prepare selection message</button><button id="clear">Clear review selections</button><span id="count" class="meta" aria-live="polite"></span></div>
<textarea id="selection" aria-label="Selection message to send for approval" readonly placeholder="Select images below, then prepare a message to send in the conversation. Nothing is approved or integrated by this page."></textarea></header>
ROWS
<footer><p>Research: <a href="../../../docs/anki-deck-01-visual-research.md">persistent research memory</a> · <a href="manifest.json">candidate manifest</a> · <a href="gallery-verification.json">gallery checks</a></p><p class="meta">Review checkboxes are temporary browser choices, not image approval. Send your selection message in the conversation to authorize integration. No assignments have been written.</p></footer></main>
<script>
const boxes=[...document.querySelectorAll('input[type=checkbox]')];
const count=()=>document.getElementById('count').textContent=boxes.filter(x=>x.checked).length+' candidate(s) selected for review';
boxes.forEach(x=>x.addEventListener('change',count));count();
document.getElementById('summarize').onclick=()=>{const ids=boxes.filter(x=>x.checked).map(x=>x.value);document.getElementById('selection').value=ids.length?'Approve these images: '+ids.join(', ')+'. Leave all other cards without images.':'No images selected. Keep all cards without images.';};
document.getElementById('clear').onclick=()=>{boxes.forEach(x=>x.checked=false);document.getElementById('selection').value='';count();};
document.getElementById('filter').onchange=e=>document.querySelectorAll('.entry').forEach(x=>x.hidden=e.target.value==='candidate'?x.classList.contains('is-gap'):e.target.value==='gap'?x.classList.contains('has-candidate'):false);
</script></html>'''
    if manifest.get('assignments_approved'):
        page = page.replace('<b>Approval pending.</b> These visuals have not been added to your deck. Pick by candidate ID, or leave any entry without an image.', '<b>Approved on 26 October 2026.</b> The user said “approve all”: these16 visuals are integrated in Deck01;14 gaps remain.')
        page = page.replace('The study package and preview remain unchanged pending approval.', 'The rebuilt study package and preview contain only the approved visuals.')
        page = page.replace('No assignments have been written.', 'Exact approved assignments are recorded in manifest.json.')
        page = page.replace('<style>', '<style>#summarize,#clear,#selection,#count {display:none !important;}')
        page = page.replace('Review checkboxes are temporary browser choices, not image approval. Send your selection message in the conversation to authorize integration.', 'The exact user approval and per-card decisions are recorded in the research memory and manifest.')
    page=page.replace('READY' ,str(ready)).replace('GAPS',str(30-ready)).replace('NAV',nav).replace('ROWS','\n'.join(rows))
    (ROOT/'index.html').write_text(page)
    print(f'Gallery: {ready} cards with candidates; {30-ready} gaps')

if __name__=='__main__':
    render()
