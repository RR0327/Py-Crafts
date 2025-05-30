"""
print('\n'.join
      ([''.join
        ([('Friendshp'[(x-y)%8]
           if((x*0.05)**2+(y*0.1)**2-1)
           **3-(x*0.05)**2*(y*0.1)
           **3<=0 else' ')
           for x in range(-30,30)])
           for y in range (15,-15,-1)]))
print("Happy Friendship Day!")
"""
# Output: A heart shape with the word "Friendshp" inside it, followed by a message "Happy Friendship Day!"
# ✅ Short Explanation of the Code
"""
The original code uses math to draw a heart-shaped curve in the terminal. It:

• Loops over a grid of (x, y) values.
• Uses a heart formula:
  ((x ⋅ 0.05)^2 + (y ⋅ 0.1)^2 - 1)^3 - (x ⋅ 0.05)^2 ⋅ (y ⋅ 0.1)^3 ≤ 0
• If a point falls inside the heart, it picks a letter from "Friendshp" using (x - y) % 8.
• If it's outside, it prints a space.
Then it prints "Happy Friendship Day!" after the heart.
"""

# Black & White Version
"""
heart_text = '\n'.join(
    ''.join(
        'Friendshp'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0
        else ' '
        for x in range(-30, 30)
    )
    for y in range(15, -15, -1)
)

print(heart_text)
print("Happy Friendship Day!")
"""
# Output: A heart shape with the word "Friendshp" inside it,
# followed by a message "Happy Friendship Day!"

# short explanation
"""
• Uses math to draw a heart shape on a grid of (x, y) points.
• Inside the heart: prints letters from "Friendshp" in a repeating pattern.
• Outside the heart: prints spaces.
• Assembles it line by line using '\n'.join(...).
• Final result is a text-based heart with "Happy Friendship Day!" at the bottom.
"""

#  Colorful Terminal Version (with ANSI Colors)
"""
import random

def colorize(char: str) -> str:
    colors = ['31', '32', '33', '34', '35', '36', '91', '92', '93', '94', '95', '96']
    color = random.choice(colors)
    return f"\033[{color}m{char}\033[0m"  # ANSI escape color codes

heart_color = '\n'.join(
    ''.join(
        colorize('Friendshp'[(x - y) % 8]) if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0
        else ' '
        for x in range(-30, 30)
    )
    for y in range(15, -15, -1)
)

print(heart_color)
print("\033[95mHappy Friendship Day!\033[0m")
"""
# Output: A colorful heart shape with the word "Friendshp" inside it,
# followed by a message "Happy Friendship Day!" in purple color.

# short explanation
"""
• Same shape and logic as Step 2.

• Adds a colorize() function that:

  • Wraps each character in ANSI escape codes for color.

  • Uses random.choice() to apply different colors.

• Result: A vibrant, rainbow-colored heart displayed in the terminal.
"""

# colorful image rendering version

import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for rendering
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Define the word to use inside the heart
text = "Friendshp"

# Create a 2D grid of x and y values
x_vals = range(-30, 30)
y_vals = range(15, -15, -1)
width, height = len(x_vals), len(y_vals)

# Prepare a 2D array to store characters
char_grid = [[' ' for _ in x_vals] for _ in y_vals]
color_grid = [['black' for _ in x_vals] for _ in y_vals]

# Define a set of colors to choose from
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'darkgreen']

# Generate heart shape using the math formula
for j, y in enumerate(y_vals):
    for i, x in enumerate(x_vals):
        formula = ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3
        if formula <= 0:
            ch = text[(x - y) % len(text)]
            char_grid[j][i] = ch
            color_grid[j][i] = random.choice(colors)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.axis('off')

# Plot each character as colored text
for j in range(height):
    for i in range(width):
        ax.text(i, height - j, char_grid[j][i], color=color_grid[j][i], fontsize=8, ha='center', va='center', family='monospace')

# Add bottom message
ax.text(width // 2, -1, "Happy Friendship Day!", fontsize=12, color='deeppink', ha='center', va='center', family='monospace')

plt.tight_layout()
output_path = os.path.join(os.getcwd(), "friendship_heart.png")
plt.savefig(output_path, dpi=300)
print(f"Image saved as {output_path}")
# Output: A colorful heart shape with the word "Friendshp" inside it,
# followed by a message "Happy Friendship Day!" displayed in a matplotlib window.
