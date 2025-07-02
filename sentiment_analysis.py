import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

def run_sentiment_analysis():
    st.header("Sentiment Analysis")
    user_input = st.text_area("Enter text to analyze sentiment:")

    if st.button("Analyze"):
        if not user_input:
            st.warning("Please enter some text.")
        else:
            try:
                # Try using the default sentiment analysis model first
                sentiment = pipeline("sentiment-analysis")
                result = sentiment(user_input)
                st.write("Sentiment Analysis Result:", result)
                st.write(f"Label: {result[0]['label']}, Score: {result[0]['score']:.2f}")
            except Exception as e:
                st.error(f"Error analyzing sentiment: {e}")
                st.info("This might be due to missing dependencies or network issues. Try installing all required packages.")

if __name__ == "__main__":
    run_sentiment_analysis()
