from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    glob="*.pdf",
    path="books",
    loader_cls=PyPDFLoader
)

document = loader.load()

print(len(document))

print(document)