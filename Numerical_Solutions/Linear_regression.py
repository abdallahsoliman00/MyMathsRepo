import numpy as np
from Numerical_Solutions.utils import Function, Linear


def calc_mse(
        x, y,
        init_mc,
        func_type: Function = Linear
    ):
    y_act = func_type(*init_mc)(x)
    err = y-y_act
    mse = np.mean(err**2)
    return mse


def grad(x, y, coords, epsilon=0.01, err_func=calc_mse, func_type=Linear):
    """Finds the gradient in n-dimensions of a function at a point"""
    args = (x,y)
    coords = np.array(coords)
    grad_vector = np.array([])
    for i in range(len(coords)):
        # for each dimension calculate the gradient
        offset = np.zeros(len(coords))
        offset[i] += epsilon    # create a vector with an offset to a coordinate e.g. [0, 0.01, 0]

        coordinates_l = coords - offset
        lower = err_func(*args, coordinates_l, func_type=func_type)

        coordinates_u = coords + offset
        upper = err_func(*args, coordinates_u, func_type=func_type)

        grad = ((upper - lower)/(2*epsilon))
        grad_vector = np.append(grad_vector, grad)
    return grad_vector


def grad_descent(x, y, init_params, alpha=0.001, epsilon=0.01, err_func=calc_mse, func_type=Linear, iteration_limit=1e5):
    coords = np.array(init_params)
    count = 0
    while True:
        gradient = grad(x, y, coords, epsilon, err_func=err_func, func_type=func_type)
        coords = coords - alpha * gradient
        count += 1
        if np.linalg.norm(gradient) < 1e-5 or count > iteration_limit:
            print("\nIterations:", count)
            return coords


if __name__ == '__main__':
    x = np.arange(-5, 6, 1)
    np.random.seed(42)
    noise = np.random.rand(len(x)) * -1.5
    y = 0.6*(np.array([-4.3, -4.5, -2, -2.6, -1.5, -0.9, 1.5, 2.1, 3.5, 3.1, 4.2]) + noise)

    print(x,y)

    print(grad(x,y,(0.6,0)))

    result = grad_descent(x, y, (0.0, 0.0))
    print("Optimal m, c:", result)
