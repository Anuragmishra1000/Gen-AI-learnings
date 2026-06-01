from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Load the model from the Hugging Face Hub
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Create a pipeline for the model
llm = HuggingFacePipeline.from_model_id(model_id, task="text-generation", pipeline_kwargs={"temperature": 1.0, "max_new_tokens": 100})

# Create a chat model
model = ChatHuggingFace(llm=llm)

# Generate a response
result = model.invoke("what is the capital of india?")
print(result.content)