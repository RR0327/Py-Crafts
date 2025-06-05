# Raw work
"""
# For handling file paths and checking if the image exists.
import os
# Used to open and process .jpg images.
from PIL import Image
import matplotlib
matplotlib.use('Agg')  # Use headless backend
# Efficiently handles pixel data as arrays.
import numpy as np
# Used to create and save the color palette as an image.
import matplotlib.pyplot as plt
# Performs clustering to find dominant colors in the image.
from sklearn.cluster import KMeans

# ✅ Hardcoded absolute path (adjust if needed)
image_path = r"D:\Vs_Code\Python_Code\ALL_Codes_Python\Own_Project_Com_Code\Py-Crafts\Others\Dipa.jpg"

print(f"Looking for image at: {image_path}")

if not os.path.exists(image_path):
    print(f"File not found at: {image_path}")
    exit(1)

print("✅ Image file found. Processing...")

# Load image using PIL
image = np.array(Image.open(image_path))

# Reshape image into a 2D array of pixels
w, h, d = image.shape
pixels = image.reshape((w * h, d))

# Apply KMeans clustering
n_colors = 10
kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(kmeans.cluster_centers_)

# Plot and save the color palette
plt.figure(figsize=(8, 2))
plt.imshow([palette])
plt.axis('off')
plt.savefig('palette.png')
print("✅ Color palette saved as 'palette.png'")
"""
# This code will extract the dominant colors from the image and save a palette image.
# Display the color palette using matplotlib and save it as 'palette.png' in the same directory.

# Explanation:
"""
• os.path.exists() checks if the image file actually exists before processing.
• Prevents the script from crashing if the file is missing.

• Opens the image using PIL, 
and converts it into a NumPy array (height x width x 3 RGB channels).
• This array is used for pixel-level manipulation.

• Flattens the 3D image array (w, h, RGB) into a 2D array of shape (num_pixels, 3).
• Each row is a single RGB color — perfect for feeding into a clustering algorithm.

• Groups all pixels into 10 clusters (dominant colors).
• kmeans.cluster_centers_ gives the average RGB value of each cluster (a dominant color).
• np.uint8() converts the values to standard 0 - 255 RGB format for visualization.

• Plots the palette as a horizontal bar of color blocks.
• plt.imshow([palette]): Shows one row of RGB blocks.
• Saves the plot to 'palette.png' — no GUI needed.

• The result is a color bar image representing the 10 most dominant colors in the original photo.
"""

# Updated version with Full error handling, RGB + HEX code printing and descriptive comments 
"""
import os
from PIL import Image
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend (for headless environments)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# === CONFIGURATION ===
# 🔧 Absolute path to the input image file (change if needed)
image_path = r"D:\Vs_Code\Python_Code\ALL_Codes_Python\Own_Project_Com_Code\Py-Crafts\Others\Dipa.jpg"
n_colors = 10  # Number of dominant colors to extract

# === CHECK IF IMAGE EXISTS ===
print(f"Looking for image at: {image_path}")
if not os.path.exists(image_path):
    print(f"Error: File not found at: {image_path}")
    exit(1)
print("✅ Image file found. Starting color extraction...")

try:
    # === LOAD IMAGE AND CONVERT TO ARRAY ===
    image = np.array(Image.open(image_path))

    # === RESHAPE IMAGE TO PIXEL LIST ===
    w, h, d = image.shape
    pixels = image.reshape((w * h, d))

    # === KMEANS CLUSTERING TO FIND DOMINANT COLORS ===
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    palette = np.uint8(kmeans.cluster_centers_)

    # === PRINT DOMINANT COLORS IN RGB AND HEX ===
    print("\nDominant Colors (Top 10):")
    for i, color in enumerate(palette):
        r, g, b = color
        hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print(f"{i+1:>2}. RGB: ({r}, {g}, {b})  HEX: {hex_code}")

    # === SAVE THE COLOR PALETTE AS AN IMAGE ===
    plt.figure(figsize=(8, 2))
    plt.imshow([palette])
    plt.axis('off')
    plt.savefig('palette.png')
    print("\n✅ Color palette saved as 'palette.png'")

except Exception as e:
    print(f"An error occurred: {e}")
"""
# This code will extract the dominant colors from the image and save a palette image.

# Key Improvements
"""
• Error handling for both file path and clustering/image conversion.
• Comments added at every major step.
• Console messages are user-friendly and clearly structured.
• RGB and HEX color codes are printed for each dominant color.
• The script is safe to run in GUI-less environments (e.g., servers, VS Code terminal only).
"""

# More modify with more features:
# Finds top 10 colors, Saves RGB and HEX codes, 
# Optional sorting by brightness, Creates a colorful HTML palette

import os
import json
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# === CONFIGURATION ===
image_path = r"D:\Vs_Code\Python_Code\ALL_Codes_Python\Own_Project_Com_Code\Py-Crafts\Others\Dipa.jpg"
n_colors = 10
sort_by_brightness = True  # Set to False to keep original clustering order

print(f"Looking for image at: {image_path}")
if not os.path.exists(image_path):
    print(f"File not found at: {image_path}")
    exit(1)

print("Image file found. Starting color extraction...")

try:
    image = np.array(Image.open(image_path))
    w, h, d = image.shape
    pixels = image.reshape((w * h, d))

    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    raw_palette = np.uint8(kmeans.cluster_centers_)

    # === RGB/HEX STRUCTURED DATA ===
    def brightness(rgb):
        r, g, b = rgb
        return 0.299*r + 0.587*g + 0.114*b

    colors = []
    for color in raw_palette:
        r, g, b = color
        hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        colors.append({
            "rgb": (int(r), int(g), int(b)),  # 🔧 Fix: ensure JSON serializable
            "hex": hex_code,
            "brightness": float(brightness((r, g, b)))  # 🔧 Convert brightness to float
        })


    if sort_by_brightness:
        colors.sort(key=lambda x: x["brightness"], reverse=True)

    # === PRINT COLORS TO CONSOLE ===
    print("\nDominant Colors (Sorted by Brightness):")
    for i, c in enumerate(colors):
        r, g, b = c["rgb"]
        print(f"{i+1:>2}. RGB: ({r}, {g}, {b})  HEX: {c['hex']}")

    # === SAVE TO TEXT FILE ===
    with open("colors.txt", "w") as f_txt:
        for i, c in enumerate(colors):
            f_txt.write(f"{i+1}. RGB: {c['rgb']}  HEX: {c['hex']}\n")
    print("Saved to 'colors.txt'")

    # === SAVE TO JSON FILE ===
    with open("colors.json", "w") as f_json:
        json.dump(colors, f_json, indent=2)
    print("Saved to 'colors.json'")

    # === GENERATE HTML FILE ===
    with open("palette.html", "w") as f_html:
        f_html.write("<html><body><h3>Dominant Colors</h3><div style='display:flex;'>\n")
        for c in colors:
            f_html.write(
                f"<div style='width:60px; height:60px; background:{c['hex']}; border:1px solid #000;'></div>\n")
        f_html.write("</div></body></html>\n")
    print("Saved HTML preview to 'palette.html'")

    # === SAVE PALETTE IMAGE ===
    plt.figure(figsize=(8, 2))
    plt.imshow([np.array([c['rgb'] for c in colors], dtype=np.uint8)])
    plt.axis('off')
    plt.savefig('palette.png')
    print("Saved color palette image as 'palette.png'")

except Exception as e:
    print(f"Error occurred: {e}")

"""
How Brightness Is Calculated:

We'll use perceived brightness:

brightness = 0.299 x R + 0.587 x G + 0.114 x B

where:
• R is the red component
• G is the green component
• B is the blue component
It prioritizes green, then red, then blue, based on human vision.
"""