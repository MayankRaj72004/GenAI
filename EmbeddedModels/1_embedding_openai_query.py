from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding model',
    dimensions=32
)

result = embedding.embed_query("Delhi is the capital of india")

print(result)