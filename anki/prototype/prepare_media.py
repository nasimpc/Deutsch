"""Download three existing images and synthesize ten German pronunciation clips."""
import asyncio
import json
from pathlib import Path
from urllib.request import Request, urlopen

import edge_tts

ROOT = Path(__file__).resolve().parent
MEDIA = ROOT / 'media'
SPEECH = [
    'ab', 'aber', 'abfahren', 'die Abfahrt', 'abgeben', 'abholen',
    'der Absender, die Absenderin', 'Achtung!', 'die Adresse', 'alle, alles',
]
IMAGES = [
    {'card': 3, 'file': 'a1_003_depart.jpg', 'url': 'https://i.imgflip.com/3984s6.jpg',
     'source': 'https://imgflip.com/memetemplate/196894518/Ight-imma-head-out',
     'description': 'SpongeBob: Ight imma head out'},
    {'card': 6, 'file': 'a1_006_pickup.jpg', 'url': 'https://i.imgflip.com/4fvc05.jpg',
     'source': 'https://imgflip.com/memetemplate/268520837/Get-in-Loser-Were-Going-Shopping',
     'description': 'Mean Girls: Get in loser, we are going shopping'},
    {'card': 8, 'file': 'a1_008_attention.jpg', 'url': 'https://i.imgflip.com/572vjn.jpg',
     'source': 'https://imgflip.com/memetemplate/314222387/Leonardo-Dicaprio-pointing',
     'description': 'Leonardo DiCaprio pointing at the screen'},
]


async def main():
    MEDIA.mkdir(exist_ok=True)
    for image in IMAGES:
        target = MEDIA / image['file']
        if not target.exists():
            request = Request(image['url'], headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(request, timeout=30) as response:
                target.write_bytes(response.read())
        print(f"Image {image['card']}: {target.stat().st_size} bytes", flush=True)
    for index, text in enumerate(SPEECH, 1):
        target = MEDIA / f'a1_{index:03}_de.mp3'
        if not target.exists():
            await edge_tts.Communicate(text, 'de-DE-KatjaNeural', rate='-10%').save(str(target))
        print(f'Audio {index}: {target.stat().st_size} bytes', flush=True)
    (ROOT / 'media-sources.json').write_text(json.dumps({
        'images': IMAGES,
        'audio': {'voice': 'de-DE-KatjaNeural', 'rate': '-10%', 'spoken_text': SPEECH},
    }, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    asyncio.run(main())
