# pip install pdf2docx
# Raw code to convert PDF to DOCX using pdf2docx library
"""
from pdf2docx import Converter
pdf_file = 'Django - Create PostgreSQL Database.pdf'
docx_file = 'Django - Create PostgreSQL Database.docx'
cv = Converter(pdf_file)
cv.conver(docx_file)
cv.close()
"""

# Modified code where we use try and except to handle errors and check if the file exists.
# pip install pdf2docx
"""
from pdf2docx import Converter

# os = Python's built-in library for Operating System interactions.
import os

# getcwd() = Get Current Working Directory
print(f" Current Working Directory: {os.getcwd()}") # Print the current working directory to check where the script is running

# Paths (since both are in the same Py-Crafts folder)
pdf_file = 'Django - Create PostgreSQL Database.pdf'
docx_file = 'Django - Create PostgreSQL Database.docx'

# Check if file exists
if not os.path.exists(pdf_file):
    print(f" Error: File '{pdf_file}' not found in current directory!")
else:
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)  # Corrected the typo from your first code
        cv.close()
        print(f" Successfully converted '{pdf_file}' to '{docx_file}'")
    except Exception as e:
        print(f" Conversion failed: {e}")
"""

# This code is modified to work no matter where you run it from.
# pip install pdf2docx
"""
from pdf2docx import Converter
import os

# Always get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# This line means:
# __file__ = The actual location of your Python script file (Convert-PDF-Docx.py)
# abspath(__file__) = Absolute path of that file
# dirname() = Take the folder of that file
# Thus BASE_DIR becomes the exact folder where your .py file exists —
# no matter where terminal is opened.

# Paths
pdf_file = os.path.join(BASE_DIR, 'Django - Create PostgreSQL Database.pdf')
docx_file = os.path.join(BASE_DIR, 'Django - Create PostgreSQL Database.docx')

# Check if file exists
if not os.path.exists(pdf_file):
    print(f" Error: File '{pdf_file}' not found!")
else:
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        print(f" Successfully converted '{pdf_file}' to '{docx_file}'")
    except Exception as e:
        print(f" Conversion failed: {e}")
"""


# Upgrade version of the code to use the multiple file conversion to docx
# pip install pdf2docx

# pip install pdf2docx
import os
from pdf2docx import Converter

def list_pdfs(directory):
    """List all PDF files in a given directory"""
    return [file for file in os.listdir(directory) if file.lower().endswith('.pdf')]    # file.lower().endswith('.pdf')	Picks only the PDF files (case-insensitive .pdf)

def select_pdf(pdfs):
    """Let user select a PDF from the list"""
    print("\nAvailable PDF files:")
    for idx, pdf in enumerate(pdfs, start=1):
        print(f"{idx}. {pdf}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the PDF you want to convert: "))
            if 1 <= choice <= len(pdfs):
                return pdfs[choice - 1]
            else:
                print(" Invalid choice. Please choose a valid number.")
        except ValueError:
            print(" Please enter a valid number.")

def convert_pdf_to_docx(pdf_path, output_path):
    """Convert selected PDF to DOCX"""
    try:
        cv = Converter(pdf_path)
        cv.convert(output_path)
        cv.close()
        print(f" Successfully converted '{pdf_path}' to '{output_path}'")
    except Exception as e:
        print(f" Conversion failed: {e}")

def main():

    # BASE_DIR ensures you always operate in the script's own folder.
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pdfs = list_pdfs(BASE_DIR)

    if not pdfs:
        print(" No PDF files found in the current directory.")
        return
    
    selected_pdf = select_pdf(pdfs)
    pdf_full_path = os.path.join(BASE_DIR, selected_pdf)
    
    output_filename = selected_pdf.replace('.pdf', '.docx')
    output_full_path = os.path.join(BASE_DIR, output_filename)
    
    convert_pdf_to_docx(pdf_full_path, output_full_path)

# Python Special Line: Ensures this file runs only when executed directly, not when imported somewhere else
if __name__ == "__main__":
    main()

# Full code Logic Flow(SImple Map):
"""
Start script ➔ List all PDFs ➔ Show menu ➔ User selects one ➔ Convert ➔ Success Message
"""
