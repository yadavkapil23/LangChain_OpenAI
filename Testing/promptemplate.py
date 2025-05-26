from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model= ChatOpenAI()

template = ChatPromptTemplate([
    ('system','You are a very helpful {domain} assistant.'),
    ('human','Explain me {topic}.'),
    ('user','Give me {type} of {topic}.'),
    # ('assistant','Give me a {method} to learn.')
    ('human','Give me {method}')
])
#Use one of 'human', 'user', 'ai', 'assistant', or 'system'.

prompt = template.invoke({'domain':'GenAI','topic':'Inheritance','type':'example','method':'trick'})

result = model.invoke(prompt)

print(prompt)
print(result)


# OUTPUT : 
# messages=[SystemMessage(content='You are a very helpful GenAI assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain me Inheritance.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Give me example of Inheritance.', additional_kwargs={}, response_metadata={}), AIMessage(content='Give me a trick to learn.', additional_kwargs={}, response_metadata={})]
# content='Sure! A common trick to remember the concept of inheritance in object-oriented programming is to think of it in terms of real-world relationships, such as parents and children. Just like how children inherit characteristics and traits from their parents, in inheritance in programming, a child class can inherit attributes and methods from a parent class.\n\nFor example, think of a class hierarchy for animals:\n\n- The parent class could be "Animal" with attributes and methods common to all animals.' \
# '\n- The child classes could be "Dog" and "Cat" which inherit from the "Animal" class and may have their own specific attributes and methods in addition to the ones inherited.' \
# '\n\nThis analogy can help you remember that inheritance involves passing down characteristics and behaviors from a more general class to more specific ones.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 153, 'prompt_tokens': 48, 'total_tokens': 201, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 
# 'id': 'chatcmpl-BbHfopSWYYFskRmF0LnRAVAD2eD6Y', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--cfde46a7-55d3-421a-8fde-3a32c4f5711d-0' usage_metadata={'input_tokens': 48, 'output_tokens': 153, 'total_tokens': 201, 'input_token_details': {'audio': 0, 'cache_read': 0}, 
# 'output_token_details': {'audio': 0, 'reasoning': 0}}