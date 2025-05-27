from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt =PromptTemplate.from_template(
    template = "Tell me 5 facts about {thing}",
    #input_variables=['thing']
)

parser = StrOutputParser()

model = ChatOpenAI()

chain = RunnableSequence(prompt,model,parser)

result = chain.invoke({"thing":"India"})

print(result)


# OUTPUT :
# 1. India is the seventh-largest country in the world by land area and the second-most populous country, with over 1.3 billion people.
# 2. India is known for its diverse culture, languages, religions, and cuisines. It is home to over 2,000 distinct ethnic groups and more than 1,600 spoken languages.
# 3. The Indian film industry, commonly referred to as Bollywood, produces the largest number of films in the world. It is also known for its vibrant music and dance scenes.
# 4. The Taj Mahal, a white marble mausoleum in Agra, India, is one of the most famous landmarks in the world and is considered a symbol of love and beauty.
# 5. India is one of the world's oldest civilizations, with a history dating back over 5,000 years. It has been home to some of the world's greatest ancient civilizations, including the Indus Valley Civilization and the Maurya and Gupta Empires.