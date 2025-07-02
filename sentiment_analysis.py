import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

st.title("Sentiment Analysis")
user_input = st.text_area("Enter text to analyze sentiment:")

if st.button("Analyze"):
    if not user_input:
        st.warning("Please enter some text.")
    else:
        sentiment = pipeline("sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis", token=hf_token)
        result = sentiment(user_input)
        st.write("Sentiment Analysis Result:",result)
        st.write(f"Label: {result[0]['label']}, Score: {result[0]['score']:.2f}")


# pipeline("task","model","token")