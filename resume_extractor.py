import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page
    doc.close()
    return text

# ✅ Use a valid file path with raw string (r"") to avoid syntax errors
pdf_path = r"C:\Users\Kratika Singh\OneDrive\RESUMES\Kratika_Singh_Resume.pdf"

# Extract and print text from the resume
resume_text = extract_text_from_pdf(pdf_path)
print("Extracted Resume Text:\n", resume_text)

