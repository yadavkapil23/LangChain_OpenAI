from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

loader = PyPDFLoader("streamlit-cheat-sheet.pdf")

document = loader.load()

print(document)

prompt = PromptTemplate.from_template(
    template = "Tell me what is in this {content}",
)

chain = prompt | model | parser

result = chain.invoke({"content":"document"})

print(result)