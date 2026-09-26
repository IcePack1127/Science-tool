import pint
from decimal import Decimal, getcontext

ureg = pint.UnitRegistry(non_int_type=Decimal)
getcontext().prec = 50

AU = ureg.Quantity(Decimal(1.496*10e8), "km")

Mj = (1.898*10e27)

r = Decimal(0.0454) * AU
Vp = Decimal(100)*ureg("m/s")
G = Decimal(6.67*10e-11)*ureg("N*m^2/kg^2")

this = (Vp**2) * r / G
print(this.to("kg"))


