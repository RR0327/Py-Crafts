# GUI based on Tkinter
"""import matplotlib.pyplot as plt
# import numpy as np  # Importing numpy as np         
rows = 5
plt.figure(figsize=(6, 6))

for i in range(rows):
    for j in range(rows-i):
        plt.scatter(j, -i, s=800, c='red')

plt.xlim(-0.5, rows - 0.5)
plt.ylim(-rows + 0.5, 0.5)

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title('Inverted Right Angled Triangle Pattern Text',
          frontsize=14)

plt.show()"""

# Non-GUI based
import matplotlib
matplotlib.use('Agg')  # Uses a non-GUI backend (no Tkinter needed).

import matplotlib.pyplot as plt

rows = 5
plt.figure(figsize=(6, 6))

for i in range(rows):
    for j in range(rows - i):
        plt.scatter(j, -i, s=800, c='skyblue')

plt.xlim(-0.5, rows - 0.5)
plt.ylim(-rows + 0.5, 0.5)

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title('Inverted Right Angled Triangle Pattern Text', fontsize=14)

# Save the output as an image
plt.savefig("inverted_triangle.png") # Saves the figure as an image instead of opening a GUI.
 
print("Plot saved as 'inverted_triangle.png'")  # Confirms the script ran successfully.

# End of code