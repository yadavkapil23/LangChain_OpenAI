from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Give me explanation of the {topic}",
    input_variables=['topic']
)


model = ChatOpenAI()

parser = StrOutputParser()

question = input("Tell me something i dont know about this.")

chain = prompt | model | parser

result = chain.invoke({"topic":question})

print(result)