from Phase_plane_plotting import *

def calc_state(prev_state, delta_t=0.01):
    x1, x2 = prev_state
    state_dt = np.array([-x1+x2**2,
                         -2*x2+3*x1**2])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

x1 = np.linspace(-1,1,20)
x2 = np.linspace(-1,1,20)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7,4))

populate_vectors(calc_state, x1, x2, ax, scale=30, normalize=True)
# calculate_path(calc_state, (1,-2), time=100)
# calculate_path(calc_state, (-1,2), color='#FFFFB3', time=100)

plt.show()
