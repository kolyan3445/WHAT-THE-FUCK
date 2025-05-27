from math import *

print('Введите Xbeg, Xend и Dx')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
x = xb
print("+--------+--------+")
print("I    X   I    Y   I")
print("+--------+--------+")
while x <= xe:
    if x < -6:
        y = 2
    elif -6 <= x <= -2:
        y = 0.25 * x + 0.5
    elif -2 <= x <= 0:
        y = -2 + sqrt(2 ** 2 + (x + 2) ** 2)
    elif 0 <= x <= 2:
        y = sqrt(2 ** 2 - (x) ** 2)
    else:
        y = -1 * x + 2
    print("I{0: 7.2f} I{1: 7.2f} I".format(x, y))
    x += dx
print("+--------+--------+")
