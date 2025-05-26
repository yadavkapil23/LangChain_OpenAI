from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

template = ChatPromptTemplate.from_messages([
    ('system','Hello👋 How its going today ?'),
    ('human',"{topic}")
])

model = ChatOpenAI()

history = []

while True:
    human_input = input("Enter your Query : ")
    if human_input == "exit":
        break
    prompt = template.invoke({'topic':human_input})

    #add the human message to the history.
    history.append(HumanMessage(content=human_input))


    #get the output by the current history.
    result = model.invoke(history)

    #print the ai output.
    print("AI : ",result.content)


X =  history.append(AIMessage(content=result.content))
print(X)
 