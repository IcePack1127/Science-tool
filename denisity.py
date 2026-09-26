import astropy.units as u
import math



def sphere_density(m ,r, unit):

    v = (4/3)*math.pi*r**3
    d = m / v
    return d.to(unit)

print(sphere_density((2.77*10**25)*u.kg, 12800*u.km, "g/cm^3"))


