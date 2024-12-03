from Phase_plane_plotting import *
from random import random, uniform


def calc_vderpol_state(prev_state, delta_t=0.01, e=0.25):
    x1, x2 = prev_state
    state_dt = np.array([x2,
                         e*(1-x1**2)*x2 - x1])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

v = np.linspace(-5, 5, 20)
v_dot = np.linspace(-6, 6, 10)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9,5))

# Plot the trajectories of n random initial conditions
n = 5
min, max = -20, 20
for i in range(n):
    calculate_path(calc_vderpol_state, [uniform(min,max), uniform(min,max)], time=20, color=(random(), random(), random()))

# Plot the trajectories of two symmetrical initial conditions
calculate_path(calc_vderpol_state, [3,6], time=15)
calculate_path(calc_vderpol_state, [-3,-6], time=15)

# Plot the vector field of the VDP oscillator
populate_vectors(calc_vderpol_state, v, v_dot, ax, scale=40)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Phase Plane Trajectory for a Van Der Pol Oscillator")
plt.xlabel("State $v$")
plt.ylabel("Rate of Change $\\dot{v}$")
plt.show()
