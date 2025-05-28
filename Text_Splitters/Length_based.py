from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("demo.pdf")

document = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 10,
    separator= " "
)

result = splitter.split_documents(document)

print(result)