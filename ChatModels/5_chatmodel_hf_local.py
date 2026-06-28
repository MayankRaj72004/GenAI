from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline

import os
os.environ['HF_HOME'] = 'D:/huggingface_cache'

from dotenv import load_dotenv
load_dotenv()


# llm = HuggingFacePipeline.from_model_id(
#     model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
# )




pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100,
    temperature=0.5,
)
llm = HuggingFacePipeline(pipeline=pipe)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result)
