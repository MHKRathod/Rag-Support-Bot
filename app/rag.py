import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load local instruction model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=100   # reduce from 256
)

# Connect to persistent Chroma DB
chroma = chromadb.PersistentClient(path="vectorstore/chroma")
collection = chroma.get_or_create_collection(name="website_docs")


def answer_question(question: str):

    print("Total documents in collection:", collection.count())

    # 1️⃣ Embed question
    query_embedding = embedding_model.encode(question).tolist()

    # 2️⃣ Retrieve top chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "answer": "I don't know",
            "sources": []
        }

    # 3️⃣ Build context
    context = "\n\n".join(documents[:3])

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the context.
If partial info exists, try to answer.

If completely missing, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    # 4️⃣ Generate answer
    response = generator(prompt)[0]["generated_text"]

    # 5️⃣ Collect sources
    sources = list(set(meta["source"] for meta in metadatas if "source" in meta))

    return {
        "answer": response.strip(),
        "sources": sources
    }