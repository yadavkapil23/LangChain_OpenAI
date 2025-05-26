from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []


messages = [
    SystemMessage(content="You are a very helpful assistant."),
]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if messages == exit:
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ",result.content)


print(chat_history)

