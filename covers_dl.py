# covers_dl.py
import requests, uuid, concurrent.futures, pathlib as p

urls = [f"https://www.crossroads-solar.com/cover{i}.jpg" for i in range(1, 11)]

def save(url):
    name = p.Path(url).name
    r = requests.get(url, timeout=15)
    (p.Path("covers") / name).write_bytes(r.content)
    print("↓", name)

p.Path("covers").mkdir(exist_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    ex.map(save, urls)
