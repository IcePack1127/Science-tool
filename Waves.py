import astropy.units as u
from math import pi


def wave(wave_variable: tuple[u.Quantity, u.Quantity], unknown: str = "0") -> u.Quantity:

    velocity: u.Quantity = [0]
    freq: u.Quantity = [0]
    wavelength: u.Quantity = [0] 

    if not velocity:
        velocity = freq*wavelength
        return velocity
    if not freq:
        freq = velocity/wavelength
        return freq
    if not wavelength:
        wavelength = velocity/freq
        return wavelength
    
    return False

speed_of_sound = 344*u.m/u.s
speed_of_light = 299792458*u.m/u.s

print('hello world')