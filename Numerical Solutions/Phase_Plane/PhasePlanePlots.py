import numpy as np
from PhasePlane import PhasePlane2D


class Pendulum(PhasePlane2D):
    def state_function(self, x1, x2):
        g,l,damping = 9.81, 2, 0.5
        return np.array([
            x2,
            -(g/l)*np.sin(x1)-damping*x2
        ])
    
    

class NewPlot(PhasePlane2D):
    def state_function(self, x1, x2):
        return np.array([
            -x1**3 + x2**2,
            -2*x1*x2 - x2
        ])
    


class Linear(PhasePlane2D):
    def state_function(self, x1, x2):
        return np.array([
            -x1 + x2,
            -x1 - x2
        ])
    


class VanDerPol(PhasePlane2D):
    def state_function(self, x1, x2):
        e=0.5
        return np.array([
            x2,
            e*(1-x1**2)*x2 - x1
        ])
    


p = Pendulum(title='Pendulum Phase Plane Plot')
p.populate_vectors(
    x1_range=(-8,8,14),
    x2_range=(-5,5,14),
    scale=30
)
ax = p.get_axes()
ax.set_xlabel("Angle $\\theta$", color='white')
ax.set_ylabel("Angular Velocity $\\dot{\\theta}$", color='white')
p.add_trajectory((1,0), 10, 500)
p.figure.tight_layout()

n = NewPlot(title="NewPlot").populate_vectors()

lin = Linear(title='Linear System').populate_vectors()

vdp = VanDerPol('Van Der Pol Oscillator')
vdp.populate_vectors(
    x1_range=(-5, 5, 20),
    x2_range=(-6, 6, 10)
)
vdp.add_trajectory((3,6), 10).add_trajectory((-3,-6), 10)

vdp.show()
