import numpy as np
import matplotlib.pyplot as plt

# Initialise variables
x = np.arange(-10, 10, 0.1)   # Define x domain
y = np.arange(-10, 10, 0.1)   # Define y domain
z = 2*x**2 + y**2

# Initialize plot
plt.style.use('dark_background')
ax = plt.axes(projection="3d")

# Plot and label 3D surface
ax.set(xlabel='x', ylabel='y', zlabel='z')
ax.plot(x, y, z)
plt.show()