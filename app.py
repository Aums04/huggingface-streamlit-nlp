
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
    try:
        from sentiment_analysis import run_sentiment_analysis
        run_sentiment_analysis()
    except ImportError as e:
        st.error(f"Error importing sentiment analysis: {e}")
    except Exception as e:
        st.error(f"Error running sentiment analysis: {e}")
elif tool == "Text Summarization":
    try:
        from summarization import run_summarization
        run_summarization()
    except ImportError as e:
        st.error(f"Error importing summarization: {e}")
    except Exception as e:
        st.error(f"Error running summarization: {e}")
elif tool == "Named Entity Recognition (NER)":
    try:
        from ner import run_ner
        run_ner()
    except ImportError as e:
        st.error(f"Error importing NER: {e}")
    except Exception as e:
        st.error(f"Error running NER: {e}")
elif tool == "Text Generation":
    try:
        from text_generation import run_text_generation
        run_text_generation()
    except ImportError as e:
        st.error(f"Error importing text generation: {e}")
    except Exception as e:
        st.error(f"Error running text generation: {e}")
elif tool == "Translation (EN to HI)":
    try:
        from translation_en_hi import run_translation
        run_translation()
    except ImportError as e:
        st.error(f"Error importing translation: {e}")
    except Exception as e:
        st.error(f"Error running translation: {e}")
elif tool == "Zero-shot Classification":
    try:
        from zero_shot import run_zero_shot
        run_zero_shot()
    except ImportError as e:
        st.error(f"Error importing zero-shot classification: {e}")
    except Exception as e:
        st.error(f"Error running zero-shot classification: {e}")
