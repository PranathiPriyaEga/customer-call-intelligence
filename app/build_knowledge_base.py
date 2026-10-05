import chromadb


CHROMA_PATH = "data/chroma_db"
KNOWLEDGE_FILE = "data/knowledge_base/it_support_knowledge.txt"


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)


collection = client.get_or_create_collection(
    name="it_support_knowledge"
)


with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
    knowledge = file.read()


sections = [
    section.strip()
    for section in knowledge.split("\n\n\n")
    if section.strip()
]


for index, section in enumerate(sections):

    collection.upsert(
        ids=[f"knowledge_{index}"],
        documents=[section]
    )


print("Knowledge base created successfully.")
print(f"Documents stored: {collection.count()}")
