from langchain_huggingface import HuggingFaceEmbeddings

from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
   "Virat Kohli is a cricket player. He is a right-handed batsman and a right-arm medium-fast bowler. He is the captain of the Indian cricket team.",
   "Rohit Sharma is a cricket player. He is a right-handed batsman and a right-arm medium-fast bowler. He is the vice-captain of the Indian cricket team.",
   "Sachin Tendulkar is a cricket player. He is a left-handed batsman and a left-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "MS Dhoni is a cricket player. He is a right-handed batsman and a right-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "Yuvraj Singh is a cricket player. He is a left-handed batsman and a left-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "Ravindra Jadeja is a cricket player. He is a left-handed batsman and a left-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "Hardik Pandya is a cricket player. He is a right-handed batsman and a right-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "Kuldeep Yadav is a cricket player. He is a left-handed batsman and a left-arm medium-fast bowler. He is the coach of the Indian cricket team.",
   "Bhuvneshwar Kumar is a cricket player. He is a right-handed batsman and a right-arm medium-fast bowler. He is the coach of the Indian cricket team.",
]

query = "tell me about virat kohli"

query_embedding = embeddings.embed_query(query)
document_embeddings = embeddings.embed_documents(documents)

scores = cosine_similarity([query_embedding], document_embeddings)[0]

index, score = (sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True))[0]
print(f"The most similar document is {documents[index]} with a score of {score}")