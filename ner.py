import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

def run_ner():
    st.header("Named Entity Recognition (NER)")
    user_input = st.text_area("Enter text for NER:")

    if st.button("Recognize Entities"):
        if not user_input:
            st.warning("Please enter some text.")
        else:
            ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple", token=hf_token)
            result = ner(user_input)
            for entity in result:
                st.write(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Score: {entity['score']:.2f}")

if __name__ == "__main__":
    run_ner()
