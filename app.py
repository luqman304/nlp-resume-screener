import streamlit as st
from scorer import score_resume

st.title("📄 NLP Resume Screener")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Score Match") and resume_file and job_description:
    score = score_resume(resume_file, job_description)
    st.write(f"🔍 Match Score: **{score:.2f}%**")