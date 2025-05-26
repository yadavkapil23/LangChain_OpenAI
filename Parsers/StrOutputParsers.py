from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

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

prompt1 = template1.invoke({"topic":"DevOps"}).to_string()

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content}).to_string()

result1 = model.invoke(prompt2)

print(result1)