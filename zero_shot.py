import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
hf_token = os.getenv("hf_token")

st.title("Zero-shot Classification")
user_input = st.text_area("Enter text for zero-shot classification:")
labels = st.text_input("Enter candidate labels (comma separated):", "education, politics, science, sports")

if st.button("Classify"):
    if not user_input or not labels:
        st.warning("Please enter both text and candidate labels.")
    else:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", token=hf_token)
        candidate_labels = [label.strip() for label in labels.split(",") if label.strip()]
        result = classifier(user_input, candidate_labels)
        st.write("## Results:")
        for label, score in zip(result['labels'], result['scores']):
            st.write(f"{label}: {score:.2f}")
