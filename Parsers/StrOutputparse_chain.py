from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(max_completion_tokens=30)

template1 = PromptTemplate(
    template = "give me a brief introduction about this : {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "Give me example of this {text}",
    input_variables=['text'],
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"DevOps"})

print(result)