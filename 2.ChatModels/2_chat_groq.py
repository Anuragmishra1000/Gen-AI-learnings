from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# GROQ_API_KEY is picked up automatically from the environment
llm = ChatGroq(model="llama-3.3-70b-versatile")

result = llm.invoke("what is the capital of india?")
print(result.content)
