import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from agent.pdf_agent import process_zip_of_pdfs
from agent.ranking_agent import rank_resumes_by_requirements
from agent.email_agent import send_emails_to_candidates

from tempfile import NamedTemporaryFile

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

st.title("Recruiting Assistant ✨")

uploaded_zip = st.file_uploader("Upload a ZIP file of resumes", type="zip")
recruiter_name = st.text_input("Recruiter Name", placeholder="e.g. John")
company_name = st.text_input("Company Name", placeholder="e.g. StarLabs")
job_title = st.text_input("Job Title / Requirements", placeholder="e.g. Java expert with 4+ years of experience")

if uploaded_zip and recruiter_name and company_name and job_title:
    with st.spinner("Processing resumes..."):
        with NamedTemporaryFile(delete=False, suffix=".zip") as tmp_zip:
            tmp_zip.write(uploaded_zip.read())
            tmp_zip_path = tmp_zip.name

        llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o", temperature=0)

        resumes = process_zip_of_pdfs(llm, tmp_zip_path)
        top = rank_resumes_by_requirements(llm, job_title, resumes)

        st.subheader("Top Candidates")
        for candidate in top:
            col1, col2, col3 = st.columns([3, 3, 2])
            col1.markdown(f"**Name:** {candidate['name']}")
            col2.markdown(f"**Email:** {candidate['email']}")
            col3.markdown(f"**Rank:** {candidate['rank']}")

            if col3.button("Send Personalized Email", key=f"send_{candidate['email']}"):
                send_emails_to_candidates([candidate], EMAIL_ADDRESS, EMAIL_PASSWORD, recruiter_name, company_name, job_title, llm)
                st.success(f"Email sent to {candidate['name']}")

        if st.button("Send Personalized Email to All"):
            send_emails_to_candidates(top, EMAIL_ADDRESS, EMAIL_PASSWORD, recruiter_name, company_name, job_title, llm)
            st.success("Emails sent to all top candidates ✅")