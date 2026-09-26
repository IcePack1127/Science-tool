from astropy import constants as const
from astropy import units as u
from astropy import coordinates as cord

angle = 20*u.microarcsecond
print(angle.to(u.lyr, equivalencies=u.parallax()))