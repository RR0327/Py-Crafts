import matplotlib
matplotlib.use('Agg')  # Add this line

import matplotlib.pyplot as plt
import numpy as np

# Generate 10,000 random points for x and y
x = np.random.random(10000)
y = np.random.random(10000)

# Create a hexbin plot (honeycomb style)
plt.hexbin(x, y, gridsize=30, cmap='plasma', edgecolors='grey')

# Add colorbar to show counts in each bin
plt.colorbar(label='Count in bin')

# Set title and axis labels
plt.title('Honeycomb Pattern Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
# Save the plot to a file
plt.savefig("Honeycomb-Pattern.png")

"""

- What is a Hexbin Plot?
    - A hexbin plot is great for visualizing the density of points when you have a lot of overlapping data points in 2D space.
    It groups nearby points into hexagonal bins, and uses color intensity to represent the number of points in each bin.

"""