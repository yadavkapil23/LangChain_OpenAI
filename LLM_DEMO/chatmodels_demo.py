from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini",temperature=1.8,max_completion_tokens=10)
#temp btata h ki kitna creative nd all.
#max complte tokens mtlb kitne tokens me hame output complete krna h

x = model.invoke("write a 5 line poem on Cricket.")

print(x)