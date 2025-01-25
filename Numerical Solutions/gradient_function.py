import numpy as np


# Finds the gradient in n-dimensions of a function at a point
def gradient(coords, func, epsilon=0.01):
    dimension = len(coords)
    coords = np.array(coords)
    grad_vector = np.array([])
    for i in range(dimension):
        # for each dimension calculate the gradient
        offset = np.zeros(dimension)
        offset[i] += epsilon    # create a vector with an offset to a coordinate e.g. [0, 0.01, 0]

        coordinates_l = coords - offset
        lower = func(*coordinates_l)

        coordinates_u = coords + offset
        upper = func(*coordinates_u)

        grad = ((upper - lower)/(2*epsilon))
        grad_vector = np.append(grad_vector, grad)
    return grad_vector


# Starting at point init_coords, the function finds the closest minimum to the initial point by "descending" the curve
def descend_slope(init_coords, func, alpha=0.01, min_norm=10**-5):
    coords = np.array(init_coords)
    count = 0
    while True:
        grad = gradient(coords, func)
        coords = coords - alpha * grad
        count += 1
        if np.linalg.norm(grad) < min_norm or count > 10**5:
            print("\nIterations:  ", count)
            return np.append(coords, func(*coords))    # Returns x,y,z coordinates of minimum point


# Finds the derivative of a 2D function given an array of discrete points
def func_grad(func_array):
    x_vals, y_vals = func_array
    epsilon = x_vals[1] - x_vals[0]

    grad = [(-25 * y_vals[0] + 48 * y_vals[1] - 36 * y_vals[2] + 16 * y_vals[3] - 3 * y_vals[4]) / (12 * epsilon)]

    for i in range(1, len(x_vals)-1):
        grad.append((y_vals[i + 1] - y_vals[i - 1])/(2*epsilon))

    grad.append((25 * y_vals[-1] - 48 * y_vals[-2] + 36 * y_vals[-3] - 16 * y_vals[-4] + 3 * y_vals[-5]) / (12 * epsilon))
    
    return [x_vals, grad]


# Finds the double derivative of a 2D function given an array of discrete points
def double_grad(func_array):
    d1 = func_grad(func_array)
    d2 = func_grad(d1)
    return d2


# Testing:
def function(x, y):
    return np.sin(0.1*x)*np.sin(0.1*y)  # Define the function here


g1 = gradient((np.pi, 3), function)
print(g1, "\tGradient vector")
print(g1/np.linalg.norm(g1), "\tUnit gradient vector")

minimum = descend_slope((-2, 0), function)
print(minimum)
