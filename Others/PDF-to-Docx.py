"""
from pdf2docx import Converter

pdf_file = "Formatted_Story_of_Microsoft.pdf"
docx_file = "Formatted_Story_of_Microsoft.docx"

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

print("Conversation completed!")
"""

import os
from pdf2docx import Converter

pdf_file = "Formatted_Story_of_Microsoft.pdf"
docx_file = "Formatted_Story_of_Microsoft.docx"

# Print all files in the folder
print("Files in current directory:")
print(os.listdir())

# Print full path of PDF file
print("Looking for:", os.path.abspath(pdf_file))

if not os.path.exists(pdf_file):
    print("❌ PDF file not found!")
else:
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print("✅ Conversion completed!")
