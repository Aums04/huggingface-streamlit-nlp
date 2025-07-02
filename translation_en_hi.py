import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

def run_translation():
    st.header("English to Hindi Translation")
    user_input = st.text_area("Enter English text to translate:")

    if st.button("Translate"):
        if not user_input:
            st.warning("Please enter some text.")
        else:
            translator = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi", token=hf_token)
            result = translator(user_input)
            st.write(result[0]['translation_text'])

if __name__ == "__main__":
    run_translation()
