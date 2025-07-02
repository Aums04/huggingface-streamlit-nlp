import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

st.title("Text Summarization")
user_input = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if not user_input:
        st.warning("Please enter some text.")
    else:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn", token=hf_token)
        result = summarizer(user_input, max_length=100, min_length=25, do_sample=False)
        st.write(result[0]['summary_text'])
