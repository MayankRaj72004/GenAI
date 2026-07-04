
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    
)

model = ChatHuggingFace(llm=llm)


# Schema
class Review(TypedDict):
    summary:str
    sentiment:str

parser = JsonOutputParser()


prompt = f"""
Extract the following review into JSON.

Return ONLY valid JSON.

Schema:
{{
    "summary":"string",
    "sentiment":"positive | negative | neutral"

}}

Review:
I recently bought the XYZ Noise Cancelling Headphones from an online store.
The delivery was very fast, and the packaging was neat and secure.
The sound quality is excellent, especially the bass and noise cancellation features.
The battery lasts for almost 28 hours on a single charge.
However, I found the ear cushions uncomfortable after two hours.
The mobile app crashed a few times.
Overall I am satisfied and would rate it 4/5.
"""

response = model.invoke(prompt)

result = parser.parse(response.content)

print(result)