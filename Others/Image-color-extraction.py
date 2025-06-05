import os
from PIL import Image
import matplotlib
matplotlib.use('Agg')  # Use headless backend
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ✅ Hardcoded absolute path (adjust if needed)
image_path = r"D:\Vs_Code\Python_Code\ALL_Codes_Python\Own_Project_Com_Code\Py-Crafts\Others\Dipa.jpg"

print(f"🔎 Looking for image at: {image_path}")

if not os.path.exists(image_path):
    print(f"❌ File not found at: {image_path}")
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

# This code will extract the dominant colors from the image and save a palette image.
# Display the color palette using matplotlib and save it as 'palette.png' in the same directory.