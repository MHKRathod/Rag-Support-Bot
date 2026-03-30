import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()
MAX_PAGES = 30   # <-- hard limit


def crawl(url, base_url, output_dir):
    global visited

    if len(visited) >= MAX_PAGES:
        return

    if url in visited:
        return

    if urlparse(url).netloc != urlparse(base_url).netloc:
        return

    # Only crawl tutorial/docs pages
    if "/tutorial" not in url and url != base_url:
        return

    print("Crawling:", url)

    visited.add(url)

    try:
        response = requests.get(url, timeout=10)
    except:
        return

    if response.status_code != 200:
        return

    os.makedirs(output_dir, exist_ok=True)

    filename = f"page_{len(visited)}.html"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        next_url = urljoin(url, link["href"])

        if any(skip in next_url.lower() for skip in [
            "#", "search", "login", "signup",
            "twitter", "linkedin", "github"
        ]):
            continue

        crawl(next_url, base_url, output_dir)