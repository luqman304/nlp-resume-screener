import pdfplumber
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def score_resume(resume_file, job_desc):
    resume_text = extract_text_from_pdf(resume_file)
    documents = [resume_text, job_desc]

    vectorizer = TfidfVectorizer().fit_transform(documents)
    score = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    return score * 100