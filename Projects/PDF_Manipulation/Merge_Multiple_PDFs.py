# This script merges multiple PDF files into a single PDF file using the PyMuPDF library (fitz).
# Raw code which not run properly for the full path of the PDF files.
"""
import fitz

def merge_pdfs(pdf_list, output_pdf):
    merged_doc = fitz.open()
    for pdf in pdf_list:
        with fitz.open(pdf) as doc:
            merged_doc. insert_pdf(doc)
            merged_doc.save(output_pdf)

pdf_list = ["Example.pdf", "Example_2.pdf"]
output_pdf = "Example_Merged.pdf"
merge_pdfs(pdf_list, output_pdf)


import fitz

def merge_pdfs(pdf_list, output_pdf):
    merged = fitz.open()
    for pdf in pdf_list:
        try:
            with fitz.open(pdf) as doc:
                merged.insert_pdf(doc)
        except FileNotFoundError:
            print(f"[!] File not found: {pdf}")
    merged.save(output_pdf)

merge_pdfs(["Example.pdf", "Example_2.pdf"], "Example_Merged.pdf")
"""
"""
import fitz
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def merge_pdfs(pdf_list, output_pdf):
    merged = fitz.open()
    for pdf in pdf_list:
        full_path = os.path.join(BASE_DIR, pdf)
        try:
            with fitz.open(full_path) as doc:
                merged.insert_pdf(doc)
        except FileNotFoundError:
            print(f"[!] File not found: {full_path}")
    merged.save(os.path.join(BASE_DIR, output_pdf))

merge_pdfs(["Example.pdf", "Example_2.pdf"], "Example_Merged.pdf")
"""

"""
Why this rocks:

Always works, no matter where you run the script from
Clean, short, and safe
Avoids annoying path errors
"""

import fitz  # PyMuPDF
import os
import datetime

def merge_all_pdfs_in_dir(output_name_prefix="Merged"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_files = [f for f in os.listdir(base_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in this directory!")
        return

    pdf_files.sort()  # Optional: merge in alphabetical order
    print(f"Found {len(pdf_files)} PDF(s): {pdf_files}")

    merged = fitz.open()
    for pdf in pdf_files:
        full_path = os.path.join(base_dir, pdf)
        try:
            with fitz.open(full_path) as doc:
                merged.insert_pdf(doc)
                print(f"✅ Merged: {pdf}")
        except Exception as e:
            print(f"Failed to open {pdf}: {e}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_pdf = os.path.join(base_dir, f"{output_name_prefix}_{timestamp}.pdf")
    merged.save(output_pdf)
    print(f"All PDFs merged into: {output_pdf}")

# LET'S ROCK
merge_all_pdfs_in_dir("ShockwavePDF")


"""
What Makes This Shockable:

Auto scans all PDFs — zero hardcoding
Clean success/fail messages
Adds a timestamp — no file overwrite issues
Alphabetical sorting — controlled merge order
Plug & Play — no extra config needed
"""