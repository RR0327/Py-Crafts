# This script splits a PDF file into individual pages and saves them as separate PDF files.
import fitz
import os

def split_pdf(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)

    for page_number in range(len(doc)):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=page_number, to_page=page_number)
        output_filename = os.path.join(output_dir, f"page_{page_number + 1}.pdf")
        new_doc.save(output_filename)

# Get the base directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# FULL PATH to the PDF
pdf_path = os.path.join(BASE_DIR, "Example.pdf")

# FULL PATH to output folder
output_dir = os.path.join(BASE_DIR, "output_pages")

# Run the function
split_pdf(pdf_path, output_dir)

"""

3-Point Summary - Split a PDF into Individual Pages

1. 🔍 Open & Prepare:

- The script uses fitz.open() from PyMuPDF to open the input PDF file.

- It automatically creates an output folder to save the split pages.

2. 📄 Loop & Split:

- It loops through each page of the PDF and creates a new PDF file for each page using insert_pdf().

3. 💾 Save Output:

- Each single-page PDF is saved as page_1.pdf, page_2.pdf, etc., inside the output directory using full path handling via os.path.join().



"""


"""
Red zone:

Your Main Question: "What am I missing till now?"
Here's your simple answer, highlighted 🔥:

❗ You're missing just this part:

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "Example.pdf")


💡 This makes the path absolute, not just relative, and it always works no matter where you run the script from.

"""

"""
🧠 Use full paths using os.path.join(BASE_DIR, "your_file.pdf") — and you're golden every time 🥇

"""