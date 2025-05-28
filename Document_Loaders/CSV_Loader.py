from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='file.csv')

docs = loader.load()

print(len(docs))
print(docs[1])