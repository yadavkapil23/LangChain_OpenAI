from langchain_community.document_loaders import WebBaseLoader

url = "https://python.langchain.com/docs/integrations/document_loaders/"

loader = WebBaseLoader(url)

documents = loader.load()

print(documents[0])