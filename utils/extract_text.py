import os
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    elif ext == '.pdf':
        return extract_pdf(file_path)
    elif ext == '.docx':
        return extract_docx(file_path)
    return ""

def extract_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

def extract_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
