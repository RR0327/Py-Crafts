# Extract images from a PDF file using PyMuPDF (fitz)
# This script extracts all images from a given PDF file and saves them to a specified directory.
# Requirements: PyMuPDF (install with `pip install PyMuPDF`) 
"""
import fitz  # PyMuPDF
import os

def extract_and_render_images(pdf_path, output_dir="images"):
    # Resolve full paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_pdf_path = os.path.join(base_dir, pdf_path)
    full_output_dir = os.path.join(base_dir, output_dir)
    os.makedirs(full_output_dir, exist_ok=True)

    # Check if file exists
    if not os.path.exists(full_pdf_path):
        print(f"[❌] File not found: {full_pdf_path}")
        return

    # Open PDF
    doc = fitz.open(full_pdf_path)
    image_found = False

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        image_list = page.get_images(full=True)

        # Extract embedded images
        if image_list:
            print(f"[] Page {page_number + 1}: {len(image_list)} image(s) found.")
            for img_index, img in enumerate(image_list, start=1):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = os.path.join(
                    full_output_dir,
                    f"page{page_number + 1}_img{img_index}.{image_ext}"
                )
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes)
                print(f"Saved embedded image: {image_filename}")
                image_found = True
        else:
            # No embedded images, so render full page
            pix = page.get_pixmap(dpi=200)
            rendered_image_path = os.path.join(
                full_output_dir, f"page{page_number + 1}_rendered.png"
            )
            pix.save(rendered_image_path)
            print(f"No embedded image, rendered page saved: {rendered_image_path}")

    doc.close()
    print(f"\nDone. All images are saved in: {full_output_dir}")

# Run the function
extract_and_render_images("Example.pdf", "images")
"""

"""
os.path.abspath(__file__): Gets the full path of the current script.

os.path.join(...): Safely builds absolute paths no matter where the script is run from.

os.makedirs(..., exist_ok=True): Creates the images/ folder if it doesn't exist.

Added safety and logging for file not found issues.

"""

"""
Extracts embedded images (like photos or scanned images)
Renders full pages as images (if no embedded image is found)
Everything is saved into the images/ folder.
"""

"""
[📄] Page 1: 1 image(s) found.
   ✅ Saved embedded image: images/page1_img1.png

[📄] Page 2: No embedded images
   🖼️ No embedded image, rendered page saved: images/page2_rendered.png

[📄] Page 3: 2 image(s) found.
   ✅ Saved embedded image: images/page3_img1.png
   ✅ Saved embedded image: images/page3_img2.png

Done. All images are saved in: D:/.../images

This output clearly tells you:

Which pages had embedded images
Which pages were rendered as full-page images (fallback)
Where the saved files are located
"""