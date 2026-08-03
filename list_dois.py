from langchain_community.vectorstores import Chroma

# Initialize Chroma vector store
vector_db = Chroma(
    persist_directory="data/funk-etal-2008.chromadb",
    collection_name="funk-etal-2008-meta",
)

# Extract metadata
metadatas = vector_db.get(include=["metadatas"])["metadatas"]

# Extract DOIs
dois = [meta["doi"] for meta in metadatas if "doi" in meta]

# Print the first two DOIs
print(dois[:2])
