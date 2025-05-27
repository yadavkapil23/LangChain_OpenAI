#jo input me milega as it is output me de dega.

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()\

passthrough = RunnablePassthrough()

print(passthrough.invoke({"name":"Kapil"}))