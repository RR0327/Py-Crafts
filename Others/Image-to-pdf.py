# With GUI

"""import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

# function to convert image to pdf
def images_to_pdf(images, pdf_name):
    if not images:  # Check if images are selected
        messagebox.showwarning("Warning", "No images selected.")
        return
    if not pdf_name:  # Check if PDF name is selected
        messagebox.showwarning("Warning", "No PDF name selected.")
        return

    try:
        # create a new file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution=100.0,
                 save_all=True, append_images=images[1:])
        messagebox.showinfo("Success",
                            "Images have been successfully converted to PDF.")
    
    except Exception as e:
        messagebox.showerror("Error",
                             "Failed to convert images to PDF.\nError: " + str(e))
        
# function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Select Images",
                                         filetypes=(("Image Files", ".jpg .jpeg .png .bmp"),
                                                    ("All files", "*.*")), initialdir= "C:/")
    return images

# function to select pdf name and path
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF As",
                                       defaultextension=".pdf", initialdir="C:/",
                                       filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    return pdf

# create GUI
root = tk.Tk()
root.title("Image to PDF Converter")
# Buttons
select_images_btn = tk.Button(root,
                              text="Select Images", command=select_images)
select_pdf_btn = tk.Button(root,
                           text="Select PDF Name", command=select_pdf)
convert_btn = tk.Button(root, text="Convert",
                        command=lambda: images_to_pdf(select_images(), select_pdf()))
# Layout
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
# Run GUI
root.mainloop()"""

# Without GUI

from PIL import Image
import os

# Function to convert images to PDF
def images_to_pdf(images, pdf_name):
    if not images:
        print("No images selected. Exiting...")
        return
    if not pdf_name:
        print("No PDF filename provided. Exiting...")
        return

    try:
        # Open first image
        pdf = Image.open(images[0])
        # Convert all images to RGB and append them
        image_list = [Image.open(img).convert("RGB") for img in images[1:]]
        pdf.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=image_list)
        print(f"Successfully converted {len(images)} images to PDF: {pdf_name}")

    except Exception as e:
        print(f"Failed to convert images to PDF. Error: {str(e)}")

# Function to get image file paths from user input
def select_images():
    image_names = input("Enter the image filenames (separated by commas): ").strip().split(',')
    images = [img.strip() for img in image_names if os.path.isfile(img.strip())]  # Ensure valid files
    if not images:
        print("No valid image files found. Please check your filenames.")
    return images

# Function to get PDF filename from user input
def select_pdf():
    pdf_name = input("Enter the output PDF filename (without extension): ").strip()
    pdf_name = pdf_name + ".pdf" if not pdf_name.endswith(".pdf") else pdf_name
    return pdf_name

# Main execution
if __name__ == "__main__":
    print("Image to PDF Converter")
    images = select_images()
    pdf_name = select_pdf()
    images_to_pdf(images, pdf_name)
