from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


llm1 =  HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)


model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz-> {quiz}',
    input_variables=['notes','quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text="""
Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression tasks.
It works by finding the optimal hyperplane that best separates data points belonging to different classes. 
The data points that are closest to the hyperplane are called support vectors, and they determine the position and orientation of the decision boundary.
SVM is highly effective for high-dimensional datasets and can handle both linear and non-linear classification problems using kernel functions such as the linear, polynomial, and radial basis function (RBF) kernels.
Due to its ability to maximize the margin between classes, SVM often provides good generalization performance and is widely used in applications like text classification, image recognition, spam detection, handwriting recognition, and bioinformatics.
"""

result = chain.invoke({'text':text})
print(result)

chain.get_graph().print_ascii()