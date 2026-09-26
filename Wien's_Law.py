import astropy.constants as const
import astropy.units as u
print("hello world")

T = 6000 * u.K
wavelength_max = const.b_wien / T
print(wavelength_max.to(u.nm))

