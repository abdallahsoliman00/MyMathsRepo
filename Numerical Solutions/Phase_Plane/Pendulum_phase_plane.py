from Phase_plane_plotting import *


def calc_pendulum_state(prev_state, delta_t=0.01, damping=0.5, l=2, g=9.81):
    x1, x2 = prev_state
    state_dt = np.array([x2,
                         -(g/l)*np.sin(x1)-damping*x2])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

theta = np.linspace(-8, 8, 14)
theta_dot = np.linspace(-5, 5, 14)

plt.style.use('dark_background')
fig, ax = plt.subplots()

calculate_path(calc_pendulum_state, [3*np.pi/2, 0], time=5, color='#FFFFB3')
calculate_path(calc_pendulum_state, [0.1, 0], time=10)
populate_vectors(calc_pendulum_state, theta, theta_dot, ax, scale=30)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Phase Plane Trajectory of a Pendulum")
plt.xlabel("Angle $\\theta$")
plt.ylabel("Angular Velocity $\\dot{\\theta}$")
plt.show()
