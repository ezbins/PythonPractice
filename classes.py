#!/usr/bin/python3
from ScaleConverter import ScaleConverter

c1 = ScaleConverter('inches', 'mm', 25)
print(c1.description())
print('converting 2 inches')
print(str(c1.convert(2))+c1.units_to)