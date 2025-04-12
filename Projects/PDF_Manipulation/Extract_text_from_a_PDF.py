# This script extracts text from a PDF file using PyMuPDF (fitz).

import fitz  # PyMuPDF
import os

def extract_text(pdf_path):
    # Get full path relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, pdf_path)

    if not os.path.exists(full_path):
        print(f"[Error] File not found: {full_path}")
        return ""
    
    try:
        with fitz.open(full_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        print(f"[Error] Failed to extract text from {pdf_path}: {e}")
        return ""

# Usage
pdf_path = "Example.pdf"  # Only filename, since full path is auto-resolved
extracted_text = extract_text(pdf_path)

if extracted_text:
    print("Text successfully extracted:\n")
    print(extracted_text)
else:
    print("No text extracted.")

"""

__file__ gets the full path of your Python script.

os.path.join(base_dir, pdf_path) builds the full absolute path to the PDF.

You no longer depend on where the script is run from — it's now script-location-safe.

"""

"""
 Output = 

Text successfully extracted:

Hello, Everyone!
I am Rakib, a cse student at BAIUST, Cumilla, Bangladesh.
I am here to learn and share my knowledge with others.
I am interested in programming, specially backend development using
python.
I am also interested in data science and machine learning.

"""