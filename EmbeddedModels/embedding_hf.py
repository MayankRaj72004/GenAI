from langchain_huggingface import HuggingFaceEmbeddings

# Load the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Single text
text = "Artificial Intelligence"

# Generate embedding
embedding = embedding_model.embed_query(text)

print("Text:", text)
print("Embedding Dimension:", str(embedding))
 