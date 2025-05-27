from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(max_completion_tokens=40,model="gpt-3.5-turbo")

model2 = ChatOpenAI(model="gpt-4o-mini")

prompt1 = PromptTemplate(
    template = "Give me a 5 line explanation of the {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = "Give me 5 questions from this {text} to solve.",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = "Combine the given topic and text into single document. \n topic -> {subject} and text -> {content}",
    input_variables=['subject','content']
)


text = "Deep learning and Transformers"


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "subject" : prompt1 | model | parser,
    "content" : prompt2 | model2 | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

X = chain.invoke({"text":text})

print(X)