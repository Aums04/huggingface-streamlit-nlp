# Streamlit Hugging Face Demos

A collection of beginner-friendly Streamlit apps demonstrating how to use Hugging Face models for various NLP tasks. This project is designed for teaching students about Streamlit and consuming Hugging Face APIs.

## Author
**Ganesh**  
[github.com/gpalve](https://github.com/gpalve)

---
Enjoy learning Streamlit and NLP with Hugging Face!

## Features
- **Text Generation** (`gpt2`)
- **Sentiment Analysis** (`distilbert-base-uncased-finetuned-sst-2-english`)
- **Translation EN→HI** (`Helsinki-NLP/opus-mt-en-hi`)
- **Named Entity Recognition (NER)** (`dslim/bert-base-NER`)
- **Summarization** (`facebook/bart-large-cnn`)
- **Zero-shot Classification** (`facebook/bart-large-mnli`)
- **Basic Streamlit Components Demo**

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/gpalve/streamlit_huggingface.git
   cd streamlit_huggingface
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Hugging Face token**
   - Copy `.env` and add your Hugging Face API token:
     ```
     hf_token=YOUR_HF_TOKEN_HERE
     ```

5. **Run any demo app**
   ```bash
   streamlit run basic.py
   # or
   streamlit run text_generation.py
   # or any other .py file
   ```

## File Overview
- `basic.py` — Demo of all major Streamlit components
- `text_generation.py` — Text generation with GPT-2
- `sentiment_analysis.py` — Sentiment analysis
- `translation_en_hi.py` — English to Hindi translation
- `ner.py` — Named Entity Recognition
- `summarization.py` — Text summarization
- `zero_shot.py` — Zero-shot classification
- `.env` — Store your Hugging Face token (not tracked by git)
- `requirements.txt` — All required Python packages
- `.gitignore` — Recommended ignores for Python/Streamlit projects


