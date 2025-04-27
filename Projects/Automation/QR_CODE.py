# Mine one
import pyqrcode
from PIL import Image

link = input("Enter anything to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale = 5)
imp = Image.open("QRCode.png")
imp.show()



"""
# Modified version
import pyqrcode
from PIL import Image

try:
    # Input for the link
    link = input("Enter anything to generate QR: ")

    # Generate QR code
    qr_code = pyqrcode.create(link)
    qr_code.png("QRCode.png", scale=5)

    # Open and display the QR code image
    img = Image.open("QRCode.png")
    img.show()

    print("QR Code generated and saved as 'QRCode.png'.")
except ModuleNotFoundError as e:
    print("Required library is missing:", e)
    print("Run 'pip install pypng' to fix this.")
except Exception as e:
    print("An error occurred:", e)


"""