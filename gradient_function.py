import numpy as np


# Finds the gradient in n-dimensions of a function at a point
def gradient(coords, func, epsilon=0.01):
    dimension = len(coords)
    coords = np.array(coords)
    grad_vector = np.array([])
    for i in range(len(coords)):
        # for each dimension calculate the gradient
        offset = np.zeros(dimension)
        offset[i] += epsilon    # create a vector with an offset to a coordinate e.g. [0, 0.01, 0]

        coordinates_l = coords - offset
        lower = func(coordinates_l[0], coordinates_l[1])

        coordinates_u = coords + offset
        upper = func(coordinates_u[0], coordinates_u[1])

        grad = ((upper - lower)/2*epsilon)*(1/epsilon**2)
        grad_vector = np.append(grad_vector, grad)
    return grad_vector


# Starting at the point init_coords the function finds the closest minimum to the initial point by "descending" the curve
def descend_slope(init_coords, func, alpha=0.01, min_norm=10**-5):
    coords = np.array(init_coords)
    count = 0
    while True:
        grad = gradient(coords, func)
        coords = coords - alpha * grad
        count += 1
        if np.linalg.norm(grad) < min_norm or count > 10**6:
            print("\nIterations:  ", count)
            return np.append(coords, func(coords[0], coords[1]))    # Returns x,y,z coordinates of minimum point


function = lambda x, y: np.sin(0.1*x)*np.sin(0.1*y)   # Define the function here

g1 = gradient((-6, -7), function)
print(g1, "\tGradient vector")
print(g1/np.linalg.norm(g1), "\tUnit gradient vector")

minimum = descend_slope((-2, 0), function)
print(minimum)
