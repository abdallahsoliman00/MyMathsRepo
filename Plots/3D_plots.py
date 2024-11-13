import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-100, 100, 0.1)   # Define x domain
y = np.arange(-100, 100, 0.1)   # Define y domain
X, Y = np.meshgrid(x, y)

# Define the function Z in terms of X and Y
# Z = X**2 * Y**2 + X**4
# Z = np.arctan(9*X/Y)
# Z = 4*(X**2/49 + Y**2/49)
Z = np.sin(0.1*X)*np.sin(0.1*Y)

# Initialize plot
plt.style.use('dark_background')
ax = plt.axes(projection="3d")

# Plot and label 3D surface
ax.set(xlabel='x', ylabel='y', zlabel='z')
ax.plot_surface(X, Y, Z, cmap='winter')
ax.scatter(5, 0, -1, marker="x", color="red")    # Add points to the 3D plot using the scatter function
plt.show()
