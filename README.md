# Phishing Email Detector

The Streamlit app classifies pasted email text using the linear SVM and TF-IDF vectorizer from the six-week project. [Open the live app](https://phishingmlproject-5rpjfvttcpev3oaizjjgef.streamlit.app/).

## Run the app locally

Use Python 3.12 in a virtual environment. Run these commands from the repository root.

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Reproduce training

The [weekly workflow](provided_code_workflow/README.md) includes the six scripts, dataset setup, and recorded results. The web app uses the fitted artifacts in `model_assets/`.
