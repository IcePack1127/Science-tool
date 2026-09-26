from scipy.integrate import solve_ivp
import time
import numpy as np
from astropy import constants as const
import Body

Body.body("A", 5000, np.array([0, 0, 0]), np.array([1.0, 0.0, 1.0]))

def ODE_system():
    pass