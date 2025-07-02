import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

st.title("Text Generation with GPT-2")
user_input = st.text_area("Enter a prompt:")

if st.button("Generate"):
    if not user_input:
        st.warning("Please enter a prompt.")
    else:
        generator = pipeline("text-generation", model="gpt2", token=hf_token)
        result = generator(user_input, max_length=100, num_return_sequences=1)
        st.write(result[0]['generated_text'])
