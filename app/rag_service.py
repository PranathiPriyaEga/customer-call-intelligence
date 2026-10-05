import chromadb


CHROMA_PATH = "data/chroma_db"


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)


collection = client.get_collection(
    name="it_support_knowledge"
)


def retrieve_knowledge(query, n_results=2):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    documents = results.get("documents", [[]])[0]

    return documents
