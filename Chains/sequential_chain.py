from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1 = PromptTemplate(
    template = "Give me an explanation of the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Give me 3 questions on this {text}",
    input_variables=['text']
)

model = ChatOpenAI(max_completion_tokens=30)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"Deep Learning"})

print(result)