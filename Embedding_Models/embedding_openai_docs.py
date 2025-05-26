from langchain_openai  import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

docs = [
    "Mumbai is financial hub of india.",
    "washington is capital of usa",
    "moscow is capital of russia."

]

result = model.embed_query(docs)

print(str(result))