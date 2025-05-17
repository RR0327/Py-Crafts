# use the Tkinter library to create a simple GUI
"""
import schemdraw    # Import the schemdraw library
import schemdraw.elements as elm    # Import the schemdraw library

d = schemdraw.Drawing() # Create a new drawing

V = d.add(elm.SourceV().label('V', loc='left')) # Voltage source
R = d.add(elm.Resistor().label('R').right())    # Resistor
C = d.add(elm.Capacitor().label('C').right())   # Capacitor
L = d.add(elm.Inductor().label('L').right())    # Inductor

d.add(elm.Ground().at(V.start)) # Ground connection at the start of the voltage source
d.add(elm.Ground().at(L.start)) # Ground connection at the start of the inductor

d.draw()    # Draw the circuit diagram
d.show()    # Show the circuit diagram
# Instead of trying to display the plot in a window (which needs Tk),
# d.save('circuit_diagram.png') # Save the circuit diagram as an image file.
# """

# use matplotlib to create a simple plot' 
# use the white background for the plot
"""
import matplotlib
matplotlib.use('Agg')  # No GUI (no Tcl/Tk)

import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

# Setup drawing
d = schemdraw.Drawing()
d.config(unit=3, fontsize=12, color='black', bgcolor='white')

# Add components
V = d.add(elm.SourceV().label('V', loc='left'))
R = d.add(elm.Resistor().label('R').right())
C = d.add(elm.Capacitor().label('C').right())
L = d.add(elm.Inductor().label('L').right())
d.add(elm.Ground().at(V.start))
d.add(elm.Ground().at(L.start))

# Draw without showing
d.draw(show=False)

# ✅ Save via plt (which holds the current figure)
plt.savefig('circuit_diagram.png', dpi=300, facecolor='white')
print("Saved 'circuit_diagram.png' with white background.")

"""


# use matplotlib to create a simple plot' 
# use the black background for the plot

"""
import matplotlib
matplotlib.use('Agg')  # ✅ Use backend that doesn't require Tcl

import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

V = d.add(elm.SourceV().label('V', loc='left'))
R = d.add(elm.Resistor().label('R').right())
C = d.add(elm.Capacitor().label('C').right())
L = d.add(elm.Inductor().label('L').right())

d.add(elm.Ground().at(V.start))
d.add(elm.Ground().at(L.start))

# Instead of trying to display the plot in a window (which needs Tk),
# we'll just save it as an image:
d.save('circuit_diagram2.png')

print("Circuit diagram saved successfully as 'circuit_diagram2.png'")
"""
