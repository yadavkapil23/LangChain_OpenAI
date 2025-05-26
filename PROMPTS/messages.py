from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage(content="You are a very helpful assistant."),
    HumanMessage(content="What is currency of America ? ")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)