from math import exp, sin, log10
from math import *
import math






# x = 1.
# print(type(x))
# print( "Expression at x=1 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

# x = 3.
# print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

# print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( math.exp(x) + 3 * math.sin(x) - math.log10(x) ) )

PEI1=9
PEI2=9.9
PEI3=10

if PEI1>=3 and PEI2>=3 and PEI3>=3:
    MEDIA = 0.3*PEI1+0.3*PEI2+0.4*PEI3
    print("MEDIA", MEDIA)
else: 
    print("nos vemos en el final")

