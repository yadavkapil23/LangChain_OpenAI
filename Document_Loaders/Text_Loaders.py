from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loaders = TextLoader("basic.txt",encoding="utf-8")

document = loaders.load()

print(document)

print(document[0])

print(document[0].page_content)

print(document[0].metadata)


prompt = PromptTemplate(
    template = "Can you explain me what is in {content}",
    input_variables=['content']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"content":"document"})

print(result)