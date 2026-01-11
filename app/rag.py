import chromadb
from chromadb.config import Settings

from sentence_transformers import SentenceTransformer

# Load the SAME embedding model used during indexing
model = SentenceTransformer("all-MiniLM-L6-v2")

chroma = chromadb.PersistentClient(
    path="vectorstore/chroma"
)
collection = chroma.get_or_create_collection(name="website_docs")


def answer_question(question: str) -> str:
    # 1. Embed the question
    query_embedding = model.encode([question]).tolist()

    # 2. Query vector DB using embedding
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return "I don't know"

    # 3. Build context
    context = "\n\n".join(documents)

    # 4. Simple grounded answer (NO OpenAI needed)
    # Since this is a docs bot, returning context is acceptable
    return context[:1000]  # limit size
