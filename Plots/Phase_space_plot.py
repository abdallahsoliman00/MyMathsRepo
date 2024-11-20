import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 2

theta_0 = np.array([-8,1])

def calc_new_state(prev_state, delta_t=0.01):

    state_dt = np.array([prev_state[1], -(g/l)*np.sin(prev_state[0])])
    new_state = prev_state + delta_t * state_dt
    
    return new_state


def calculate_path(init_state, time=5, plot=True, color='#FFFFFF'):
    state_array = np.array([init_state])

    old_state = np.array(init_state)
    for i in range(0, time*100):
        new_state = calc_new_state(old_state)
        state_array = np.append(state_array, [new_state], axis=0)
        old_state = new_state

    state_array = state_array.T

    if plot:
        plt.plot(state_array[0], state_array[1], color=color)
        plt.scatter(init_state[0], init_state[1], 15, marker='.', color=color)
        plt.scatter(state_array.T[-1][0], state_array.T[-1][1], 15, marker='x', color=color)
        return state_array
    else:
        return state_array



theta = np.linspace(-10, 10, 20)
theta_dot = np.linspace(-10, 10, 20)


plt.style.use('dark_background')
fig, ax = plt.subplots()

calculate_path(theta_0, time=8)
calculate_path([1, 1])

for i in theta:
    for j in theta_dot:
        # Starting point (x, y) and vector components (dx, dy)
        state_direction = calc_new_state([i, j]) - np.array([i,j])
        ax.quiver(i, j, state_direction[0], state_direction[1], color='blue', width=0.003, scale=2, headwidth=2)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Phase Plane Solution of a Pendulum")
plt.xlabel("Angle $\\theta$")
plt.ylabel("Angular Velocity $\\ddot{\\theta}$")
plt.show()