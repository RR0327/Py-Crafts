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


