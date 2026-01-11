import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from app.chunker import chunk_text

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma = chromadb.PersistentClient(
    path="vectorstore/chroma"
)


collection = chroma.get_or_create_collection(name="website_docs")

def embed_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"source": filepath}],
            ids=[f"{filepath}_{i}"],
            embeddings=[embeddings[i]]
        )

if __name__ == "__main__":
    cleaned_dir = "data/cleaned"

    for file in os.listdir(cleaned_dir):
        embed_file(os.path.join(cleaned_dir, file))

    print("✅ Local embeddings stored successfully")
