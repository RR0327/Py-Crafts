from pdf2docx import Converter

pdf_file = "Merge.pdf"
docx_file = "Merge.docx"

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

print("Conversation completed!")