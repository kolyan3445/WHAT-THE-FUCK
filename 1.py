from math import *

x = float(input('Введите значение x: '))
z1 = (sin(4 * x)) / (1 + cos(4 * x)) * (cos(2 * x) / (1 + cos(2 * x)))
print("{0:.2f} {1:.4f} ".format(x, z1))
z2 = cos((3/2) * pi - x) / (sin(3/2) * pi - x)
print("{0:.2f} {1:.4f}".format(x, z2))
