from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='users.csv')

data = loader.load()

print(data[0])
