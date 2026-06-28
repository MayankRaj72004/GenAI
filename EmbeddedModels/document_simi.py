from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()


# Load the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is one of the greatest batsmen in cricket history.",
    "Lionel Messi is an Argentine football player and World Cup winner.",
    "Python is a popular programming language used in AI and Machine Learning.",
    "The Taj Mahal is one of the Seven Wonders of the World.",
    "MS Dhoni is a former captain of the Indian cricket team."
]

query = "Tell me about virat kohli"


doc_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

result = cosine_similarity([query_embedding],doc_embeddings)
index,score=sorted(list(enumerate(result)),key=lambda x:x[1])[-1]

print(documents[index])