import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 200)   # Define x domain
y = np.linspace(-5, 5, 200)  # Define y domain
X, Y = np.meshgrid(x, y)

"""
# Define the function Z in terms of X and Y:
# Examples:
Z = X**2 * Y**2 + X**4
Z = np.arctan(9*X/Y)
Z = 4*(X**2/49 + Y**2/49)
Z = X*np.sin(0.15*Y) + Y*np.sin(0.15*X)
Z = -6*X*Y - 3*Y**2 - X**2
"""
Z = np.arctan(9*X/Y)


# Initialize plot
plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Disable camera rolling
def disable_roll(event):
    azim, elev = ax.azim, ax.elev
    ax.view_init(elev=elev, azim=azim, roll=0)

# Connect to motion_notify_event
fig.canvas.mpl_connect('motion_notify_event', disable_roll)

# Plot and label 3D surface
ax.set(xlabel='x', ylabel='y', zlabel='z')
ax.plot_surface(X, Y, Z, cmap='tab20c')
# ax.scatter(5, 0, -1, marker="x", color="red")    # Add points to the 3D plot using the scatter function
plt.show()
