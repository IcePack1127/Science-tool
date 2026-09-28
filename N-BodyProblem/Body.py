from scipy.integrate import solve_ivp
import time
import numpy as np
from astropy import constants as const

class body:
    def __init__(self, name: str, mass: float, velocity: np.ndarray, coordinate: np.ndarray) -> None:
        self.name = name
        self.mass = mass
        self.velocity = velocity
        self.coordinate = coordinate

    def accel(self, r):
        accel = (self.mass*const.G)/(r**2)

        return accel
