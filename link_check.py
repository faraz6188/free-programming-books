# link_check.py
import requests, re, sys
from bs4 import BeautifulSoup

root = sys.argv[1] if len(sys.argv) > 1 else "https://www.crossroads-solar.com"
html = requests.get(root).text
urls = {a["href"] for a in BeautifulSoup(html, "html.parser").find_all("a", href=True)}
for u in urls:
    try:
        r = requests.head(u, allow_redirects=True, timeout=10)
        if r.status_code >= 400:
            print("❌", u, r.status_code)
    except Exception as e:
        print("⚠️ ", u, e)
