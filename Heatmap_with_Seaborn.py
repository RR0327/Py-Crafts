"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
data = np.random.rand(10, 10)   # 10 rows, 10 columns

sns.heatmap(data, cmap= 'coolwarm', annot=True, fmt=" .2f")

plt.show()
"""

import matplotlib
matplotlib.use('Agg')  # Add this line

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
data = np.random.rand(10, 10)   # 10 rows, 10 columns
# Create a heatmap
sns.heatmap(data, cmap= 'coolwarm', annot=True, fmt=" .2f")
# Set the title and labels
plt.show()
# Save the plot to a file
plt.savefig("heatmap.png")

"""
This code generates a heatmap using the Seaborn library in Python.
• It first imports the necessary libraries: numpy, matplotlib, and seaborn.

• What it does:

    • sns.heatmap(...): Draws the heatmap using the random data.

    • cmap='coolwarm': Uses a red-blue color gradient (cool to warm colors).

    • annot=True: Annotates each cell with its value.

    • fmt=" .2f": Formats each number in the cell with 2 decimal places.

"""

"""
• What is a Heatmap (with Seaborn)?
    - A heatmap is a 2D visualization that uses color to represent values in a matrix, allowing for quick identification of patterns, variations, and anomalies.
    - This leverages the brain's faster processing of color compared to numerical data.

• Seaborn's Heatmap in Simple Terms:
    • Seaborn's heatmap() is a powerful and beautiful tool to:
        • Create a color-coded grid from a 2D array or DataFrame.
        • Warm, red, or dark colors can represent high values.
        • Cool, light blue colors often represent low values.
        • Use `annot=True` to display values inside each box.

"""

"""
Summary:

Concept	         Meaning
Heatmap	        Visual grid where colors represent numeric values
Seaborn	        Python library that makes heatmaps easy, beautiful, and customizable
Why Use It?	    Helps spot trends, clusters, highs/lows, and outliers at a glance
Data Format	    Requires a 2D array (NumPy or Pandas DataFrame)
"""