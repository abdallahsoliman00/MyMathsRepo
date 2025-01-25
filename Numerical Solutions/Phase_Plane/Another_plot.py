from Phase_plane_plotting import *

# def calc_state(prev_state, delta_t=0.001):
#     x1, x2 = prev_state
#     state_dt = np.array([-x1**3+x2**2,
#                          -2*x1*x2 - x2])
#     new_state = prev_state + delta_t * state_dt
    
#     return new_state

def calc_state(prev_state, delta_t=0.001):
    x1, x2 = prev_state
    state_dt = np.array([-x1 + x2,
                         -x1 - x2])
    new_state = prev_state + delta_t * state_dt
    
    return new_state

x1 = np.linspace(-2,2,25)
x2 = np.linspace(-2,2,25)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7,4))

populate_vectors(calc_state, x1, x2, ax, scale=50, normalize=True)
# calculate_path(calc_state, (-0.5,0), time=500)
# calculate_path(calc_state, (-10,30), color='#FFFFB3', time=100)

plt.show()
