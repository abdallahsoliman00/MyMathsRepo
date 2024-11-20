import numpy as np
import matplotlib.pyplot as plt

sigma = 10
beta = 8/3
rho = 50


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

init_point = (-20,5,-3)
x,y,z = init_point

states = calculate_path(init_point, time=60)
ax.scatter(x,y,z, marker=".", color="#8DD3C7")
ax.plot(states[0], states[1], states[2], linewidth=0.7)
plt.show()