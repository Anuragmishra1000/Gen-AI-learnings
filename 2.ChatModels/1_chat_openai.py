import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Using Nebius AI (OpenAI-compatible)
# ChatOpenAI works with any OpenAI-compatible endpoint via base_url + api_key.
llm = ChatOpenAI(
    model=os.environ["NEBIUS_MODEL"],
    base_url=os.environ["NEBIUS_BASE_URL"],
    api_key=os.environ["NEBIUS_API_KEY"],
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    temperature=1.6,
    max_completion_tokens=10
)

result = llm.invoke("write a 5 line poem on cricket")
print(result.content)
