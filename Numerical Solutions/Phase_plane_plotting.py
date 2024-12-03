import numpy as np
import matplotlib.pyplot as plt


# Time in seconds
def calculate_path(state_calc, init_state, time=5, plot=True, color='#8DD3C7'):
    state_array = np.array([init_state])

    old_state = np.array(init_state)
    for i in range(0, time*100):
        new_state = state_calc(old_state)
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

# ax refers to the axes to plot on
def populate_vectors(state_calc, x1, x2, ax, scale=2, normalize=True):

    for i in x1:
        for j in x2:
            # Starting point (x, y) and vector components (dx, dy)
            state_direction = state_calc([i, j]) - np.array([i,j])
            if normalize:
                r = (state_direction[0]**2 + state_direction[1]**2)**0.5
            else:
                r = 1
            ax.quiver(i, j, state_direction[0]/r, state_direction[1]/r, color='blue', width=0.003, scale=scale, headwidth=2)

