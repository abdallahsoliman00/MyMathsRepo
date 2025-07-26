import numpy as np


def gradient(coords, func, epsilon=0.01):
    """Finds the gradient in n-dimensions of a function at a point"""
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


def descend_slope(init_coords, func, alpha=0.01, min_norm=10**-5):
    """Starting at point init_coords, the function finds the closest minimum to the initial point by "descending" the curve"""
    coords = np.array(init_coords)
    count = 0
    while True:
        grad = gradient(coords, func)
        coords = coords - alpha * grad
        count += 1
        if np.linalg.norm(grad) < min_norm or count > 10**5:
            print("\nIterations:  ", count)
            return np.append(coords, func(*coords))    # Returns x,y,z coordinates of minimum point


def func_grad(func_array) -> list[list[float]]:
    """Finds the derivative of a 2D function given an array of discrete points"""
    x_vals, y_vals = func_array
    epsilon = x_vals[1] - x_vals[0]

    grad = [(-25 * y_vals[0] + 48 * y_vals[1] - 36 * y_vals[2] + 16 * y_vals[3] - 3 * y_vals[4]) / (12 * epsilon)]

    for i in range(1, len(x_vals)-1):
        grad.append((y_vals[i + 1] - y_vals[i - 1])/(2*epsilon))

    grad.append((25 * y_vals[-1] - 48 * y_vals[-2] + 36 * y_vals[-3] - 16 * y_vals[-4] + 3 * y_vals[-5]) / (12 * epsilon))
    
    return [x_vals, grad]


def double_grad(func_array):
    """Finds the double derivative of a 2D function given an array of discrete points"""
    d1 = func_grad(func_array)
    d2 = func_grad(d1)
    return d2


def find_zeros(coords):
    """Returns the roots or zeros of any 2D function given the x and y coordinates"""
    x,y = coords
    zero_crossings = np.where(np.diff(np.sign(y)))[0]

    zeros = []
    for i in zero_crossings:
        x0 = x[i]
        x1 = x[i+1]
        y0 = y[i]
        y1 = y[i+1]
        zero = x0 - y0 * (x1 - x0) / (y1 - y0)
        zeros.append(zero)

    return zeros


def find_stationary_points(coords):
    """Returns the x-coordinates the stationary points of any 2D function"""
    grad_coords = func_grad(coords)
    zeros = find_zeros(grad_coords)
    # TODO: return the actal stationary point, not just the x value of the stationary point
    return zeros



# Testing:
if __name__ == "__main__":
    def function(x, y):
        return np.sin(0.1*x)*np.sin(0.1*y)  # Define the function here


    g1 = gradient((np.pi, 3), function)
    print(g1, "\tGradient vector")
    print(g1/np.linalg.norm(g1), "\tUnit gradient vector")

    minimum = descend_slope((-2, 0), function)
    print(minimum)

    import matplotlib.pyplot as plt

    def func(x):
        x = np.array(x)
        return np.sin(x) + 0.5*np.cos(3*x)

    x = np.linspace(0,4*np.pi, 200)
    y = func(x)

    sp = find_stationary_points([x,y])
    print(sp)

    plt.grid(True)
    plt.plot(x,y)
    plt.plot(*func_grad([x,y]))
    plt.scatter(sp, func(sp))
    plt.show()
