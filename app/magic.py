import openai
import os

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

chat = ChatOpenAI(temperature=0.0, model_name='gpt-4-32k')

template_string = """
You are a legal expert in the Italian legal system.
Please provide a succinct summary which highlights the key points of the
following legal document delimited by triple backticks in simple Italian terms:
${text}`
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

def simplify(parsed_document):
    customer_messages = prompt_template.format_messages(
                        text=parsed_document)
    response = chat(customer_messages)
    return response.content
