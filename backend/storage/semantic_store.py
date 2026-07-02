import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_PERSIST_DIR

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)

collection_name = "equity_chunks"

# Lazy-loaded embedding function
_embedding_fn = None


def get_embedding_fn():
    """
    Lazily initialize the SentenceTransformer embedding model.
    This prevents loading the model during application startup,
    reducing memory usage on Render.
    """
    global _embedding_fn

    if _embedding_fn is None:
        print("Loading SentenceTransformer embedding model...")
        _embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        print("SentenceTransformer model loaded successfully.")

    return _embedding_fn


def get_collection():
    """
    Returns the ChromaDB collection, creating it if necessary.
    """
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=get_embedding_fn()
    )


def add_chunks(texts: list, metadatas: list, ids: list):
    """
    Add embedded documents to ChromaDB.
    """
    print(f"add_chunks: start with {len(texts)} chunks")

    try:
        collection = get_collection()

        print("add_chunks: adding documents to ChromaDB")

        collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

        print("add_chunks: completed successfully")

    except Exception as e:
        print(f"add_chunks: ERROR - {type(e).__name__}: {e}")
        raise


def search_chunks(query: str, n_results: int = 5):
    """
    Search ChromaDB using semantic similarity.
    """
    print(f"search_chunks: querying '{query}'")

    try:
        collection = get_collection()

        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )

        response = {
            "documents": results["documents"][0] if results.get("documents") else [],
            "metadatas": results["metadatas"][0] if results.get("metadatas") else [],
            "distances": results["distances"][0] if results.get("distances") else [],
        }

        print(f"search_chunks: found {len(response['documents'])} results")

        return response

    except Exception as e:
        print(f"search_chunks: ERROR - {type(e).__name__}: {e}")
        raise