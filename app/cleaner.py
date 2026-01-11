import os
import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

if __name__ == "__main__":
    input_dir = "data/raw_pages"
    output_dir = "data/cleaned"
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
            cleaned = clean_text(f.read())

        with open(os.path.join(output_dir, file), "w", encoding="utf-8") as f:
            f.write(cleaned)
