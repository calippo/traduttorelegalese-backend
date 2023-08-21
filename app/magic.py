import openai
import os

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

chat = ChatOpenAI(temperature=0.0)

template_string = """Simplify the text that is delimited by triple backticks \
text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

def simplify(parsed_document):
    customer_messages = prompt_template.format_messages(
                        text=parsed_document)
    response = chat(customer_messages)
    return response.content
