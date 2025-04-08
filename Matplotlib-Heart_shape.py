"""import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

plt.fill(x, y, 'red')
plt.axis("off")
plt.show()"""


import matplotlib  
matplotlib.use('Agg')  # Add this line  

import numpy as np  
import matplotlib.pyplot as plt  

t = np.linspace(0, 2 * np.pi, 100)  
x = 16 * np.sin(t) ** 3  
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)  

plt.fill(x, y, 'RED')  
plt.axis("off")  
plt.savefig('heart_shape.png')  # Save the plot to a file
