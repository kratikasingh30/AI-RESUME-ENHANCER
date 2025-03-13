import streamlit as st
from resume_extractor import extract_text_from_pdf
from resume_analyzer import analyze_resume, improve_bullet_points

st.title("AI Resume Enhancer & Career Advisor")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("Resume Analysis & Suggestions")
    analysis = analyze_resume(resume_text)
    st.write(analysis)
    
    st.subheader("Enhanced Bullet Points")
    improved_text = improve_bullet_points(resume_text)
    st.write(improved_text)
