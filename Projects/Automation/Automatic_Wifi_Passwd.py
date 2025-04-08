"""import wifi_qrcode_generator as qr

qr.wifi_qrcode('Leader', False, 'WPA', 'password')"""


"""# Import the required module
import wifi_qrcode_generator as qr
import matplotlib.pyplot as plt
from PIL import Image

# Generate the Wi-Fi QR code
wifi_qr = qr.wifi_qrcode(ssid='Leader', hidden=False, authentication_type='WPA', password='password')

# Save the QR code as an image (optional)
wifi_qr.save("wifi_qrcode.png")

# Display the QR code using PIL
image = Image.open("wifi_qrcode.png")
plt.imshow(image)
plt.axis('off')  # Turn off axis
plt.show()
"""

"""# Import the required module
import wifi_qrcode_generator as qr
import matplotlib.pyplot as plt
from PIL import Image

# Generate the Wi-Fi QR code
try:
    print("Generating Wi-Fi QR Code...")
    wifi_qr = qr.wifi_qrcode(ssid='Leader', hidden=False, authentication_type='WPA', password='password')

    # Save the QR code as an image
    wifi_qr.save("wifi_qrcode.png")
    print("QR Code saved as wifi_qrcode.png")

    # Display the QR code using PIL
    image = Image.open("wifi_qrcode.png")
    plt.imshow(image)
    plt.axis('off')  # Turn off axis
    plt.show()
except Exception as e:
    print("An error occurred:", e)"""



"""# Import the required module
import wifi_qrcode_generator as qr
from PIL import Image
import matplotlib.pyplot as plt

try:
    print("Generating Wi-Fi QR Code...")
    # Generate the Wi-Fi QR code
    wifi_qr = qr.wifi_qrcode(ssid='Leader', hidden=False, authentication_type='WPA', password='password')

    # Convert the QR code to an image
    qr_image = wifi_qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file
    qr_image.save("wifi_qrcode.png")
    print("QR Code saved as wifi_qrcode.png")

    # Display the QR code
    plt.imshow(qr_image)
    plt.axis('off')  # Turn off axis
    plt.show()

except Exception as e:
    print("An error occurred:", e)
"""


# Final Code for generating Wifi_QR_Code

import wifi_qrcode_generator as qr
from PIL import Image

try:
    print("Generating Wi-Fi QR Code...")
    wifi_qr = qr.wifi_qrcode(ssid='Periwinkle-5G', hidden=False, authentication_type='WPA', password='periwinkle5*')
    qr_image = wifi_qr.make_image(fill_color="black", back_color="white")
    qr_image.save("wifi_qrcode.png")
    print("QR Code saved as wifi_qrcode.png")
except Exception as e:
    print("An error occurred:", e)
