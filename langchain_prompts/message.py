from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY", ""),
    temperature=0.1,
)

messages = [
    SystemMessage('You are a helpful assistant'),
    HumanMessage('Tell me about LangChain')
]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)