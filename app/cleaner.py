import os
from bs4 import BeautifulSoup


def extract_visible_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove unwanted elements
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # Remove extra spaces
    lines = [line.strip() for line in text.splitlines()]
    clean_text = " ".join(line for line in lines if line)

    return clean_text


def clean_all():
    input_dir = "data/raw_pages"
    output_dir = "data/cleaned"

    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
            raw_html = f.read()

        cleaned = extract_visible_text(raw_html)

        with open(os.path.join(output_dir, file), "w", encoding="utf-8") as f:
            f.write(cleaned)

    print("✅ Cleaning completed successfully.")