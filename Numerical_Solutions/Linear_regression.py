import numpy as np


x = np.arange(-5, 6, 1)
np.random.seed(42)
noise = np.random.rand(len(x)) * -1.5
y = 0.6*(np.array([-4.3, -4.5, -2, -2.6, -1.5, -0.9, 1.5, 2.1, 3.5, 3.1, 4.2]) + noise)

print(x,y)


def calc_mse(x, y, init_mc):
    m,c = init_mc
    y_act = m*x +c
    err = y-y_act
    mse = np.sum(err**2)
    return mse

# Finds the gradient in n-dimensions of a function at a point
def grad(x , y, coords, epsilon=0.01):
    args = (x,y)
    coords = np.array(coords)
    grad_vector = np.array([])
    for i in range(2):
        # for each dimension calculate the gradient
        offset = np.zeros(2)
        offset[i] += epsilon    # create a vector with an offset to a coordinate e.g. [0, 0.01, 0]

        coordinates_l = coords - offset
        lower = calc_mse(*args, coordinates_l)

        coordinates_u = coords + offset
        upper = calc_mse(*args, coordinates_u)

        grad = ((upper - lower)/(2*epsilon))
        grad_vector = np.append(grad_vector, grad)
    return grad_vector


def grad_descent(x, y, init_mc, alpha=0.001, epsilon=0.01):
    coords = np.array(init_mc)
    count = 0
    while True:
        gradient = grad(x, y, coords, epsilon)
        coords = coords - alpha * gradient
        count += 1
        if np.linalg.norm(gradient) < 1e-5 or count > 10000:
            print("\nIterations:", count)
            return coords

print(grad(x,y,(0.6,0)))

result = grad_descent(x, y, (0.0, 0.0))
print("Optimal m, c:", result)
