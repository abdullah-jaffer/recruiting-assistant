import os
import zipfile
import tempfile
import fitz  # PyMuPDF
from typing import List
from model.Candidate import Candidate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel


def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def process_zip_of_pdfs(llm, zip_path: str):

    if not zip_path.endswith('.zip'):
        raise ValueError("Only .zip files are supported.")

    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"{zip_path} is not a valid zip file.")

    results = []

    with tempfile.TemporaryDirectory() as temp_dir:

        with zipfile.ZipFile(zip_path, 'r') as archive:
            archive.extractall(temp_dir)

        pdf_files = []
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.lower().endswith('.pdf') and not file.startswith('._'):
                    full_path = os.path.join(root, file)
                    pdf_files.append(full_path)


        for pdf_file in pdf_files:
            try:
                text = extract_text_from_pdf(pdf_file)

                prompt = f"""
Extract the following information from this candidate's resume:
- Full name
- Email address
- Phone number
- Work experience in full text form
- Total years of experience
- Highest education level (e.g., Bachelor's, Master's, PhD)

Resume:
{text}
"""
                structured_llm = llm.bind_tools([Candidate])
                structured_output = structured_llm.invoke(prompt)
                args = structured_output.tool_calls[0]['args']
                results.append(args)

            except Exception as e:
                print(f"Error processing {pdf_file}: {e}")

    return results