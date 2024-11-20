import numpy as np
import matplotlib.pyplot as plt


# Define x domain
x = np.arange(0, 8*np.pi, 0.01)

# Define f(x) or y
y1 = 2 * np.sin(x**2) * np.exp(-0.5*x)
y2 = 0.0001*(np.exp(-0.5*x) + x**3*np.sin(5*x))

# Plot x and y
plt.plot(x, y1, color='#0000FF', label='Graph 1')
plt.plot(x, y2, color='#FF00FF', label='Graph 2')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.legend()
plt.show()