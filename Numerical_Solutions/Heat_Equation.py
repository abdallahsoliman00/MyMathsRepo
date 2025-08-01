import numpy as np
import matplotlib.pyplot as plt


dt = 0.01
time = 10
t_vals = np.arange(0, time, dt)
n_tsteps = len(t_vals)

x_points = np.linspace(0, 10, 101)
x_size = len(x_points)

# Initial Conditions

# T0 = [1 if n < 5 else -1 for n in x_points]
# init_cond = []
# for x in x_points:
#     if x < 4:
#         init_cond.append(-1)
#     elif x >= 4 and x < 8:
#         init_cond.append(1)
#     else:
#         init_cond.append(-x+9)
# T0 = np.array(init_cond)

T0 = [np.exp(-0.05 * x) * (2 * np.sin(0.5 * x) + 4 * np.sin(x) + np.sin(7 * x))
      for x in x_points]

# T0 = -1/5*x_points + 1


def calc_heat_evolution(init_cond, timesteps, source=0, sink=0):
    """Numerical calculation of evolution"""
    time_evolution = []

    alpha = 0.75
    prev_T = init_cond
    for _ in range(timesteps):
        new_T = np.zeros(len(init_cond))

        if source:
            new_T[0] = prev_T[0] + alpha*((prev_T[1] + source)/2 - prev_T[0])
        else:
            new_T[0] = prev_T[0] + alpha*(prev_T[1] - prev_T[0])

        if sink:
            new_T[-1] = prev_T[-1] + alpha*((prev_T[-2] + sink)/2 - prev_T[-1])
        else:
            new_T[-1] = prev_T[-1] + alpha*(prev_T[-2] - prev_T[-1])

        for i in range(1, len(T0)-1):
            new_T[i] = prev_T[i] + alpha*((prev_T[i+1] + prev_T[i-1])/2 - prev_T[i])


        time_evolution.append(list(new_T))
        prev_T = new_T

    time_evolution = np.array(time_evolution)
    return time_evolution

evo = calc_heat_evolution(T0, n_tsteps, 1,-1)

time_grid, x_grid = np.meshgrid(t_vals, x_points, indexing='ij')

# Plotting
plt.style.use('dark_background')
ax = plt.axes(projection="3d")

plt.title("Heat Equation Time Evolution")
ax.set(xlabel='$x$', ylabel='$t$', zlabel='$T$')
ax.plot_surface(x_grid, time_grid, evo, cmap='plasma')
plt.show()
