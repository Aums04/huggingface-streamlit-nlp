
import streamlit as st

st.set_page_config(
    page_title="Hugging Face Demos",
    page_icon="🤗",
    layout="wide"
)

st.title("Hugging Face NLP Demos with Streamlit")
st.markdown("Welcome to this collection of Natural Language Processing (NLP) demos powered by Hugging Face models and Streamlit. Select a tool from the sidebar to get started.")

# Sidebar for tool selection
st.sidebar.title("NLP Tools")
tool = st.sidebar.selectbox("Choose a tool:", (
    "Sentiment Analysis",
    "Text Summarization",
    "Named Entity Recognition (NER)",
    "Text Generation",
    "Translation (EN to HI)",
    "Zero-shot Classification"
))

# Conditionally import and run the selected tool's code
if tool == "Sentiment Analysis":
    from sentiment_analysis import run_sentiment_analysis
    run_sentiment_analysis()
elif tool == "Text Summarization":
    from summarization import run_summarization
    run_summarization()
elif tool == "Named Entity Recognition (NER)":
    from ner import run_ner
    run_ner()
elif tool == "Text Generation":
    from text_generation import run_text_generation
    run_text_generation()
elif tool == "Translation (EN to HI)":
    from translation_en_hi import run_translation
    run_translation()
elif tool == "Zero-shot Classification":
    from zero_shot import run_zero_shot
    run_zero_shot()
