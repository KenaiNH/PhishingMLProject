import streamlit as st
from phishing_detector import classify_email

st.title("Phishing Email Detector")
st.caption("Paste a sample email to try the Logistic Regression model.")

with st.form("email_form"):
    email = st.text_area("Email body", height=200)
    submitted = st.form_submit_button("Classify email")

if submitted:
    try:
        label = classify_email(email)
    except ValueError as exc:
        st.warning(str(exc))
    else:
        st.write(f"Prediction: **{label}**")
