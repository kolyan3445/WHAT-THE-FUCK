from math import *

x = float(input('Введите значение x: '))
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
print('Значение функции:', y)

