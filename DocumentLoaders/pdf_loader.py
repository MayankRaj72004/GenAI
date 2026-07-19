from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader = PyPDFLoader('roadmap.pdf')

docs = loader.load()


# chain = prompt | model | parser

# result = chain.invoke({'poem':docs[0].page_content})

# print(result)

print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)




