"""
PhasePlane2D
------------
This file contains a dummy class `PhasePlane2D` to aid in plotting 2D state space systems.

Example Usage
-------------
To create a new Phase Plane plot, create a new class that inherits from `PhasePlane2D`
and define a state function of your own in a function called `state_function()`::

    class NewPlot(PhasePlane2D):
        def state_function(self, x1, x2):
            return np.array([
                -x1**3 + x2**2,
                -2*x1*x2 - x2
            ])

"""
from typing import Tuple, Optional, Sequence

import numpy as np
import matplotlib.pyplot as plt


RANGE_SPECIFIER = Tuple[float, float, int]


class PhasePlane2D:
    
    def __init__(
        self,
        title: Optional[str] = None,
        facecolor: str = 'black',
        foregroundcolor: str = 'white',
        showgrid: bool = True,
        **kwargs
    ):
        self.figure = plt.figure(num=self.__class__.__name__, figsize=(7,4),  facecolor=facecolor, **kwargs)
        self.ax = self.figure.add_subplot(1,1,1, facecolor=facecolor)
        
        # For more control over the grid and title see `self.get_axes()`
        if showgrid:
            self.ax.grid(True, linestyle='--', linewidth=0.5)

        if title:
            self.ax.set_title(title, color=foregroundcolor)

        self.ax.tick_params(colors=foregroundcolor)
        for spine in self.ax.spines.values():
            spine.set_color(foregroundcolor)


    def show(self, **kwargs):
        plt.show(**kwargs)

    
    def get_axes(self):
        """Should be used to allow user to edit the axes, lnestyles an other axes attributes.
        The title, foreground (text and axes) color, facecolor and grid are all configurable
        from within the __init__ function.
        The remaining attributes should be edited by calling this function.
        
        Example
        -------
        To add annotations to the plot::

            P = PhasePlane2D()
            ax = P.get_axes()
            ax.annotate("Annotaton", (0,0))

        """
        return self.ax


    def state_function(
        self,
        x1: float,
        x2: float
    ):
        """This is the defining vector/function of the state space.
        It is to be implemented by the user.
        
        Example
        -------
        ::

            def state_function(self, x1, x2):
                return np.array([
                    -x1**3 + x2**2,
                    -2*x1*x2 - x2
                ])
        
        Where `x1` and `x2` are the two tracked states of the system at any given moment in time.
        """
        return np.array([
            x1 + x2,
            x1 + x2
        ])
    

    def calc_next_state(self, prev_state, dt):
        """Returns the next state given a state"""
        state_dt = self.state_function(*prev_state)
        return prev_state + dt * state_dt
        

    def calculate_path(self, initial_state, time, timesteps):
        """Calculates the trajectory of a given inital condition
        Returns a 2D array containing all x1 and x2 values."""
        # TODO: Make the calculation accurate.
        # i.e. Calculate the path for the actual amount of time elapsed.
        # Include time in the calculation. Look at the pendulum example to help. 
        dt = time/timesteps
        trajectory = [np.array(initial_state)]
        old_state = np.array(initial_state)

        for _ in range(timesteps):
            new_state = self.calc_next_state(old_state, dt)
            trajectory.append(new_state)
            old_state = new_state

        state_array = np.array(trajectory).T
        return state_array
    

    def add_trajectory(
        self,
        initial_state: Sequence[float],
        time: float = 5,
        timesteps:int = 1000,
        color: str = "#EFFDBB",
        **kwargs
    ):
        """Adds a trajectory for a certain period of time for an initial condition in the state space.

        Indicates the starting point with a '.' and the end point with an 'x'.
        
        Parameters
        ----------
        initial_state : Sequence[float]
            The initial state of the system given in coordinate form.
        time : float
            The amount of time that the trajectory should be calculated for.
        timesteps : int
            The number of timesteps that should be used to calculate the trajectory.
        color : str
            The color of the trajectory.
        **kwargs : None
            Keyword arguments to be passed into the `plot()` function.

        Example Usage
        -------------
        ::

            p = PhasePlane2D()
            p.add_trajectory((1,0), 5, 500, '#000FFF')
            p.show()

        Notes
        -----
        - Multiple trajectories can be added to the same plot.
        """
        trajectory = self.calculate_path(initial_state, time, timesteps)
        self.ax.plot(*trajectory, color=color, **kwargs)
        self.ax.scatter(*initial_state, s=15, color=color, marker='.')          # Initial state marked by .
        self.ax.scatter(*trajectory[:,-1], s=15, color=color, marker='x')       # Final state marked by x
        return self
    

    def populate_vectors(
            self,
            x1_range: RANGE_SPECIFIER = (-8, 8, 14),
            x2_range: RANGE_SPECIFIER = (-8, 8, 14),
            color: str = "#0000FF",
            scale: float = 30, 
            normalize: bool = True,
            **arrow_kwargs
    ):
        x1 = np.linspace(*x1_range)
        x2 = np.linspace(*x2_range)

        for i in x1:
            for j in x2:
                # Starting point (x, y) and vector components (dx, dy)
                state_direction = self.calc_next_state([i, j], dt=0.001) - np.array([i,j])
                if normalize:
                    r = (state_direction[0]**2 + state_direction[1]**2)**0.5
                else:
                    r = 1
                self.ax.quiver(i, j, state_direction[0]/r, state_direction[1]/r, color=color, width=0.003, scale=scale, **arrow_kwargs)

        return self

