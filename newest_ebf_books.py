# newest_ebf_books.py
# Data source: https://api.github.com/repos/EbookFoundation/free-programming-books/contents/books
import requests, pathlib, datetime, json, os

API = "https://api.github.com/repos/EbookFoundation/free-programming-books/contents/books"
DEST = pathlib.Path("free_books")
DEST.mkdir(exist_ok=True)

for item in requests.get(API, timeout=15).json():
    if item["type"] == "file" and item["name"].endswith(".md"):
        local = DEST / item["name"]
        if not local.exists() or datetime.datetime.fromisoformat(
            item["updated_at"].replace("Z", "+00:00")
        ) > datetime.datetime.fromtimestamp(local.stat().st_mtime, tz=datetime.timezone.utc):
            local.write_text(requests.get(item["download_url"], timeout=15).text)
            print("↓", item["name"])
