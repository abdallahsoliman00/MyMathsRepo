import numpy as np
import matplotlib.pyplot as plt
from random import uniform, random

sigma = 10
beta = 8/3
rho = 28


def calc_new_state(prev_state, delta_t=0.005):
    # State vector for the Lorenz attractor
    state_dt = np.array([sigma*(prev_state[1] - prev_state[0]),
                         prev_state[0]*(rho - prev_state[2]) - prev_state[1],
                         prev_state[0]*prev_state[1] - beta*prev_state[2]])
    
    new_state = prev_state + delta_t * state_dt
    
    return new_state


def calculate_path(init_state, time=50):
    state_array = np.array([init_state])

    old_state = np.array(init_state)
    for i in range(0, time*200):
        new_state = calc_new_state(old_state)
        state_array = np.append(state_array, [new_state], axis=0)
        old_state = new_state

    state_array = state_array.T

    return state_array
    

# Initialize plot
plt.style.use('dark_background')
ax = plt.axes(projection="3d")

# Plot and label 3D surface
ax.set(xlabel='x', ylabel='y', zlabel='z')

for i in range(10):
    init_point = (uniform(-20,20),uniform(-5,5),uniform(-3,3))
    x,y,z = init_point
    color = (random(), random(), random())
    states = calculate_path(init_point, time=60)
    ax.scatter(x,y,z, marker=".", color=color)
    ax.plot(states[0], states[1], states[2], linewidth=0.7, color=color)

# init_point2 = (-20,5,-3.001)
# x2,y2,z2 = init_point2
# states2 = calculate_path(init_point2, time=60)
# ax.scatter(x2,y2,z2, marker=".", color="#0000FF")
# ax.plot(states2[0], states2[1], states2[2], linewidth=0.7, color="blue")

plt.show()