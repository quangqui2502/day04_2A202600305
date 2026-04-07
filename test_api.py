import os   
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini")
print(llm.invoke("Hello, how are you?").content)
