from langchain_huggingface import HuggingFaceEmbeddings

# Load the model from the Hugging Face Hub
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Embed a text
text = "Delhi is the capital of India"
embedding = embeddings.embed_query(text)
print(embedding)

# Embed a list of texts
texts = ["Delhi is the capital of India", "Mumbai is the financial capital of India", "Bangalore is the IT capital of India"]
embeddings = embeddings.embed_documents(texts)
print(embeddings)