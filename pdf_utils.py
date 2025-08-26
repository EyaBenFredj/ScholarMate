# pdf_utils.py

import fitz  # PyMuPDF
import pdfplumber
import re
import pandas as pd


def extract_text_from_pdf(pdf_path):
    """
    Extract clean text from a PDF using PyMuPDF.
    """
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"


def extract_sections(text):
    """
    Split text into sections based on common academic paper headers.
    """
    sections = {}
    current_section = "Unknown"
    lines = text.split('\n')

    for line in lines:
        clean_line = line.strip()
        # Match common section headers more robustly
        if re.match(r"^(abstract|introduction|background|method|materials|results|discussion|conclusion|reference|acknowledg)", clean_line.lower()):
            current_section = clean_line
            sections[current_section] = ""
        else:
            sections.setdefault(current_section, "")
            sections[current_section] += clean_line + "\n"

    return sections


def extract_tables_from_pdf(pdf_path):
    """
    Extract tables from a PDF using pdfplumber.
    Each table is returned as a Pandas DataFrame.
    """
    tables = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_tables = page.extract_tables()
                for table in extracted_tables:
                    # Clean and convert to DataFrame if valid
                    if table and any(any(cell for cell in row) for row in table):
                        df = pd.DataFrame(table)
                        tables.append(df)
    except Exception as e:
        tables.append(pd.DataFrame([["Error extracting tables", str(e)]]))
    return tables
