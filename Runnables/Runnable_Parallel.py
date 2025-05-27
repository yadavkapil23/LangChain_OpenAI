from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI()

prompt1 = PromptTemplate.from_template(
    template = "Generate a Twitter Post on {topic}",
)

prompt2 = PromptTemplate.from_template(
    template = "Generate a Linkedin Post on {topic}",
)

parallel_chain = RunnableParallel({ #makes a runnable parallel of both
    "tweet" : RunnableSequence(prompt1,model,parser),  #first pipeline/chain to generate tweet that runs simulatneously.
    "linkedin" : RunnableSequence(prompt2,model,parser),   #second pipeline/chain to generate linkedin post.
})

result = parallel_chain.invoke({"topic": "AI"})

print(result)



# OUTPUT : 
# {'tweet': '"Excited to see how #AI continues to revolutionize industries and improve efficiency. The possibilities are endless! #artificialintelligence"', 
#  'linkedin': 'Exciting news in the world of AI! As technology continues to advance, Artificial Intelligence is playing a crucial role in shaping our future. From improving efficiency in industries to enhancing customer experiences, AI is revolutionizing the way we live and work. I am thrilled to be a part of this innovative field and look forward to seeing how AI will continue to transform the world. #AI #ArtificialIntelligence #Innovation #Technology #FutureOfWork'}