import chromadb

client = chromadb.PersistentClient(path="D:/Chroma/Cybersecurity")

from datetime import datetime

from chromadb import Documents, EmbeddingFunction, Embeddings

class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        # embed the documents somehow
        return embeddings



collection = client.create_collection(
    name="Cybersecurity",
    embedding_function=emb_fn,
    metadata={
        "description": "my first Chroma collection",
        "created": str(datetime.now())
    }
)
