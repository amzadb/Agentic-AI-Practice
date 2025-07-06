import streamlit as st
from docx import Document
from PyPDF2 import PdfReader
from fpdf import FPDF
import tempfile
import os

# --- Helper functions ---

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith('.docx'):
        return extract_text_from_docx(uploaded_file)
    elif uploaded_file.name.endswith('.pdf'):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.doc'):
        st.warning("DOC files are not fully supported. Please use DOCX or PDF.")
        return ""
    else:
        st.error("Unsupported file type.")
        return ""

def extract_text_from_linkedin(link):
    # Stub: In production, use LinkedIn API or scraping (with permission)
    return f"Extracted profile info from {link} (stub)"

def ai_redesign_resume(content, template):
    # Stub: Replace with actual AI call (OpenAI, Gemini, etc.)
    # For now, just insert content into template
    return template.replace("{{CONTENT}}", content)

def save_pdf(text, filename):
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

# --- Predefined template ---
TEMPLATE = """
RESUME

Name: [Your Name]
Contact: [Your Contact Info]
LinkedIn: [Your LinkedIn]

Summary:
{{CONTENT}}

Skills:
- Skill 1
- Skill 2

Experience:
- Company 1: Role, Dates
- Company 2: Role, Dates

Education:
- Degree, School, Year

References available upon request.
"""

# --- Streamlit UI ---
st.title("AI Resume Redesign Agent")

uploaded_file = st.file_uploader("Upload your resume (.doc, .docx, .pdf)", type=["doc", "docx", "pdf"])
linkedin_link = st.text_input("Or enter your LinkedIn profile link")

if st.button("Redesign Resume"):
    if uploaded_file:
        content = extract_text_from_file(uploaded_file)
    elif linkedin_link:
        content = extract_text_from_linkedin(linkedin_link)
    else:
        st.warning("Please upload a file or enter a LinkedIn link.")
        st.stop()

    if not content.strip():
        st.error("No content extracted from the input.")
        st.stop()

    redesigned_resume = ai_redesign_resume(content, TEMPLATE)
    st.markdown("### Redesigned Resume Preview")
    st.markdown(f"```\n{redesigned_resume}\n```")

    # Save as PDF and offer download
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        save_pdf(redesigned_resume, tmpfile.name)
        st.download_button(
            label="Download as PDF",
            data=open(tmpfile.name, "rb").read(),
            file_name="redesigned_resume.pdf",
            mime="application/pdf"
        )
        os.unlink(tmpfile.name)