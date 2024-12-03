from Phase_plane_plotting import *

def calc_state(prev_state, delta_t=0.01):
    x1, x2 = prev_state
    state_dt = np.array([-x1**3 + x2**2,
                         -2*x1*x2 - x2])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

x1 = np.linspace(-10,10,18)
x2 = np.linspace(-10,10,18)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7,4))

populate_vectors(calc_state, x1, x2, ax, scale=50)
calculate_path(calc_state, (5,3))
calculate_path(calc_state, (-5.5,-3), color='#FFFFB3')

plt.show()
