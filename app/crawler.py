import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

visited = set()
MAX_PAGES = 30   # 👈 HARD LIMIT

def crawl(url, base_url, output_dir):
    if url in visited or len(visited) >= MAX_PAGES:
        return

    visited.add(url)

    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return

        soup = BeautifulSoup(res.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)
        filename = url.replace("https://", "").replace("/", "_") + ".txt"

        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
            f.write(text)

        for link in soup.find_all("a", href=True):
            next_url = urljoin(base_url, link["href"])
            if urlparse(next_url).netloc == urlparse(base_url).netloc:
                crawl(next_url, base_url, output_dir)

    except Exception:
        pass


if __name__ == "__main__":
    os.makedirs("data/raw_pages", exist_ok=True)
    start_url = "https://fastapi.tiangolo.com/"
    crawl(start_url, start_url, "data/raw_pages")
