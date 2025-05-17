# Use UPC type only
"""
import barcode
from barcode.writer import ImageWriter

number = input("Enter the code to generate barcode : ")
barcode_format = barcode.get_barcode_class('upc')
my_barcode = barcode_format(number, writer=ImageWriter())
my_barcode.save("generated_barcode")

from PIL import Image
Image.open('generated_barcode.png')
"""

# Using the all supported types:
#   ean8, ean13, upc, isbn10, isbn13,
#   issn, code39, code128, pzn, jan

import barcode
from barcode.writer import ImageWriter
from PIL import Image

# List of supported barcode types
supported_types = [
    "ean8", "ean13", "upc", "isbn10", "isbn13",
    "issn", "code39", "code128", "pzn", "jan"
]

print("Supported Barcode Types:")
for i, code in enumerate(supported_types, 1):
    print(f"{i}. {code}")

# User selects barcode type
while True:
    try:
        choice = int(input("Select a barcode type by number (e.g., 3 for upc): "))
        if 1 <= choice <= len(supported_types):
            selected_type = supported_types[choice - 1]
            break
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid number.")

# Get the barcode class
barcode_format = barcode.get_barcode_class(selected_type)

# Ask user for code input
while True:
    number = input(f"Enter the code for {selected_type} (check its digit length): ")
    try:
        # Try to create the barcode object
        my_barcode = barcode_format(number, writer=ImageWriter())
        break
    except Exception as e:
        print(f"Error: {e}. Please try again with a valid code.")

# Save the barcode image
filename = my_barcode.save("generated_barcode")
print(f"Barcode generated and saved as: {filename}.png")

# Open the image using Pillow
Image.open(filename + ".png").show()

"""
Barcode Types with Example Inputs
=====================================

| Barcode Type | Input Length / Format      | Example Input    | Notes / Use Case                                 |
| ------------ | -------------------------- | ---------------- | ------------------------------------------------ |
| upc        | 11 digits              | 12345678901    | Standard retail products (mostly in USA)         |
| ean13`     | 12 digits              | 590123412345   | International retail barcodes (adds check digit) |
| isbn13     | 12 digits              | 978316148410   | Book identifiers (ISBN)                          |
| code128    | Variable, alphanumeric | Code128-XYZ123 | High-density, supports letters, digits, symbols  |
| code39     | Variable, alphanumeric | CODE39-1234    | Simple alphanumeric (uppercase, -, space, etc.)  |
| issn       | 7 digits               | 2049363        | International Standard Serial Number (magazines) |
| jan        | 12 digits              | 490123456789   | Japanese Article Number (like EAN13 for Japan)   |
| pzn        | 6 digits               | 123456         | German pharmaceutical product code               |
| ean8       | 7 digits               | 1234567        | Shorter retail codes, smaller packaging          |
| isbn10     | 9 digits               | 316148410      | Book ISBN (older 10-digit format)                |

"""