"""import PyPDF2
import pyttsx3
import pdfplumber

pdf_filename = input("Enter the PDF file name (including extension): ").strip()

try:
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        speak = pyttsx3.init()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                speak.say(text)
                speak.runAndWait()

        speak.stop()
        print("AudioBook creation completed.")
except FileNotFoundError:
    print("The specified file not found.")
except Exception as e:
    print(f"An error occured: {e}")"""




import PyPDF2
import pyttsx3

pdf_filename = input("Enter the PDF file name (including extension): ").strip()

try:
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        speak = pyttsx3.init()

        print("Extracting and converting text to audio...")
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            if text.strip():  # Check if the page has text
                print(f"Reading page {page_num + 1}...")
                speak.say(text)
                speak.runAndWait()
            else:
                print(f"Page {page_num + 1} has no readable text.")

        speak.stop()
        print("AudioBook creation completed.")
except FileNotFoundError:
    print("The specified file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
