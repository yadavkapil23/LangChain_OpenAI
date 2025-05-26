from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


template = ChatPromptTemplate([
  ('system','You are a very helpful {domain} expert.'),
  ('human','Explain me this {topic} in an {level} way.')
])

prompt = template.invoke({'domain':"Generative AI","topic":"Machine Learning","level":"Easy"})


model = ChatOpenAI()
result = model.invoke(prompt)

print(prompt)

print(result)


# OUTPUT - 
# messages=[SystemMessage(content='You are a very helpful Generative AI expert.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain me this Machine Learning in an Easy way.', additional_kwargs={}, response_metadata={})]
# content="Sure! Machine learning is like teaching a computer to learn how to do something without explicitly programming it to do so. Just like how a baby learns from examples and experiences, a machine learning algorithm learns patterns and relationships from data. " \
# "The computer uses these patterns to make predictions or decisions without being explicitly told what to do for every scenario. " \
# "It's like the computer is learning and improving on its own through practice and feedback, making it really powerful for a wide range of tasks like image recognition, language translation, and even self-driving cars."
# additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 106, 'prompt_tokens': 32, 'total_tokens': 138, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
#  'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BbHJY8tZNMhphEVv2je1Y5vDKSj80', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} 
# id='run--4a30f694-aaf8-4351-aabe-cf03ce8b4a69-0' usage_metadata={'input_tokens': 32, 'output_tokens': 106, 'total_tokens': 138, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}