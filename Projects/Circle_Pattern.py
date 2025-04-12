# Circle Pattern Plot
"""
import matplotlib   # Importing matplotlib for plotting
matplotlib.use('Agg')  # Use a non-interactive backend (for headless environments)

import numpy as np
import matplotlib.pyplot as plt

# Circle parameters
radius = 1
num_points = 50
theta = np.linspace(0, 2 * np.pi, num_points)

# Compute x and y points
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, color='black', s=50)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes
ax.set_title("Circle pattern plot")  # Fix: was incorrectly written as `ax.title`

# Save the figure to a file instead of displaying it
plt.savefig("circle_pattern.png", bbox_inches='tight', dpi=300)

# If you want to confirm it's saved:
print("Plot saved as circle_pattern.png")
"""

# Color Gradient Circle
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

radius = 1
num_points = 50
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
colors = plt.cm.viridis(np.linspace(0, 1, num_points))

fig, ax = plt.subplots()
ax.scatter(x, y, color=colors, s=50)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Color Gradient Circle")
plt.savefig("color_gradient_circle.png", bbox_inches='tight', dpi=300)
"""

# Rose Curve (Petal Pattern)
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)
k = 5  # Number of petals if k is odd
r = np.cos(k * theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y, color='red')
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Rose Curve (k=5)")
plt.savefig("rose_curve.png", bbox_inches='tight', dpi=300)
"""

# Spiral Pattern
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

num_points = 200
theta = np.linspace(0, 4 * np.pi, num_points)
r = np.linspace(0.1, 1, num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y, color='purple')
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Spiral Pattern")
plt.savefig("spiral_pattern.png", bbox_inches='tight', dpi=300)
"""

# 3D Circle (with sine Z axis)
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

radius = 1
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='cyan')
ax.set_title("3D Circle with Sin Wave Height")
plt.savefig("3d_circle.png", bbox_inches='tight', dpi=300)
"""

# Circle with Varying Point Size
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

radius = 1
num_points = 50
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
sizes = 50 + 30 * np.sin(theta)

fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', s=sizes)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Varying Point Sizes")
plt.savefig("variable_size_circle.png", bbox_inches='tight', dpi=300)
"""

# Animated Breathing Circle (GIF)
"""
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

theta = np.linspace(0, 2 * np.pi, 50)
fig, ax = plt.subplots()
sc = ax.scatter([], [], s=50)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

def update(frame):
    r = 1 + 0.2 * np.sin(frame / 10)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    sc.set_offsets(np.c_[x, y])
    return sc,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
ani.save("animated_breathing_circle.gif", writer=PillowWriter(fps=20))
"""

# Interactive Circle with Plotly
"""
import numpy as np
import pandas as pd
import plotly.express as px

radius = 1
theta = np.linspace(0, 2 * np.pi, 50)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({'x': x, 'y': y})
fig = px.scatter(df, x='x', y='y', title="Interactive Circle Pattern")
fig.update_traces(marker=dict(size=10, color='black'))
fig.write_html("interactive_circle.html")
print("Interactive plot saved to interactive_circle.html")
"""


# Circle Art Generator Toolkit: A collection of circle-based patterns and animations.
"""
— a beautiful combination of:

Static plots

3D plotting

Mathematical patterns

Animations

Interactivity
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for all static plots
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import pandas as pd

# Ensure output directory
output_dir = "/mnt/data/circle_art_outputs"
os.makedirs(output_dir, exist_ok=True)

# 1. Color Gradient Circle
def plot_color_gradient_circle():
    radius = 1
    num_points = 50
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    colors = plt.cm.viridis(np.linspace(0, 1, num_points))
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=colors, s=50)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Color Gradient Circle")
    plt.savefig(f"{output_dir}/color_gradient_circle.png", bbox_inches='tight', dpi=300)
    plt.close()

# 2. Rose Curve
def plot_rose_curve():
    theta = np.linspace(0, 2 * np.pi, 1000)
    k = 5
    r = np.cos(k * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Rose Curve (k=5)")
    plt.savefig(f"{output_dir}/rose_curve.png", bbox_inches='tight', dpi=300)
    plt.close()

# 3. Spiral Pattern
def plot_spiral():
    num_points = 200
    theta = np.linspace(0, 4 * np.pi, num_points)
    r = np.linspace(0.1, 1, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='purple')
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Spiral Pattern")
    plt.savefig(f"{output_dir}/spiral_pattern.png", bbox_inches='tight', dpi=300)
    plt.close()

# 4. 3D Circle (sine Z)
def plot_3d_circle():
    radius = 1
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.sin(theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='cyan')
    ax.set_title("3D Circle with Sin Wave Height")
    plt.savefig(f"{output_dir}/3d_circle.png", bbox_inches='tight', dpi=300)
    plt.close()

# 5. Varying Point Size
def plot_variable_size_circle():
    radius = 1
    num_points = 50
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    sizes = 50 + 30 * np.sin(theta)
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', s=sizes)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Varying Point Sizes")
    plt.savefig(f"{output_dir}/variable_size_circle.png", bbox_inches='tight', dpi=300)
    plt.close()

# 6. Animated Breathing Circle
def generate_breathing_animation():
    theta = np.linspace(0, 2 * np.pi, 50)
    fig, ax = plt.subplots()
    sc = ax.scatter([], [], s=50)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    def update(frame):
        r = 1 + 0.2 * np.sin(frame / 10)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        sc.set_offsets(np.c_[x, y])
        return sc,

    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    ani.save(f"{output_dir}/animated_breathing_circle.gif", writer=PillowWriter(fps=20))
    plt.close()

# 7. Interactive Plotly Circle
def plot_interactive_circle():
    radius = 1
    theta = np.linspace(0, 2 * np.pi, 50)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    df = pd.DataFrame({'x': x, 'y': y})
    fig = px.scatter(df, x='x', y='y', title="Interactive Circle Pattern")
    fig.update_traces(marker=dict(size=10, color='black'))
    fig.write_html(f"{output_dir}/interactive_circle.html")

# Run all plots
plot_color_gradient_circle()
plot_rose_curve()
plot_spiral()
plot_3d_circle()
plot_variable_size_circle()
generate_breathing_animation()
plot_interactive_circle()


# Local-friendly file list printout
print("✅ All visualizations have been saved in the 'circle_art_outputs' folder:")
for file in os.listdir(output_dir):
    print("   -", file)


"""
What Makes This Unique:
✅ Blends mathematics + programming + design

✅ Exports in PNG, GIF, and HTML formats

✅ Usable for data science, educational demos, or creative projects

✅ You now have a base to build apps, games, or visual art generators

"""

"""

You've just made a:

Modular Visualization Toolkit

That combines math, art, interactivity, and animation

All in a single script with reusable components
"""