from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Tool")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY", ""),
    temperature=0.1,
)

paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical",
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)",
])

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=(
        'You are an expert AI researcher. Explain the research paper "{paper_input}" '
        "in a {style_input} style. Provide a {length_input} explanation covering the "
        "key contributions, methodology, and impact of the paper."
    ),
)

if st.button("Summarize"):
    try:
        st.text("Summarizing...")
        prompt = template.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        })
        response = model.invoke(prompt)
        st.write(response.content)
    except Exception as e:
        st.error(f"Error: {str(e)}")
