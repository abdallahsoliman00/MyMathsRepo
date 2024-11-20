import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 2
damping_coeff = 0.2

theta = np.linspace(-20, 20, 25)
theta_dot = np.linspace(-15, 15, 20)


def calc_new_state(prev_state, delta_t=0.01):

    state_dt = np.array([prev_state[1], -(g/l)*np.sin(prev_state[0])-damping_coeff*prev_state[1]])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

# Time in seconds
def calculate_path(init_state, time=5, plot=True, color='#8DD3C7'):
    state_array = np.array([init_state])

    old_state = np.array(init_state)
    for i in range(0, time*100):
        new_state = calc_new_state(old_state)
        state_array = np.append(state_array, [new_state], axis=0)
        old_state = new_state

    state_array = state_array.T

    if plot:
        plt.plot(state_array[0], state_array[1], color=color)
        plt.scatter(init_state[0], init_state[1], 15, marker='.', color=color)                  # Initial state marked by .
        plt.scatter(state_array.T[-1][0], state_array.T[-1][1], 15, marker='x', color=color)    # Final state marked by x
        return state_array
    else:
        return state_array


plt.style.use('dark_background')
fig, ax = plt.subplots()

calculate_path([20,-10], time=12, color='#FFFFB3')
calculate_path([5, 6], time=12)

for i in theta:
    for j in theta_dot:
        # Starting point (x, y) and vector components (dx, dy)
        state_direction = calc_new_state([i, j]) - np.array([i,j])
        ax.quiver(i, j, state_direction[0], state_direction[1], color='blue', width=0.003, scale=2, headwidth=2)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Phase Plane Trajectory of a Pendulum")
plt.xlabel("Angle $\\theta$")
plt.ylabel("Angular Velocity $\\ddot{\\theta}$")
plt.show()