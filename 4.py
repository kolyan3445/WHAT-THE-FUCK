# Шаг 1: Запрос количества элементов массива (не более 30)
n = int(input("Введите количество элементов массива (не более 30): "))
if n > 30:
    print("Количество элементов не должно превышать 30. Установлено значение 30.")
    n = 30

# Шаг 2: Создание массива с убывающими случайными значениями в диапазоне [-5.0, 5.0]
arr = []

a = float(input("Введите значение a от -5.0 до 5.0: "))
if -5.0 > a or a > 5.0:
    print("Значение вне диапазона -5.0, 5.0. Приводим к ближайшему...")
    if a < -5:
        a = -5.0
    elif a > 5:
        a = 5.0

b = float(input("Введите значение b от -5.0 до 5.0: "))
if (-5.0 > b or b > 5.0) and b != a:
    print("Значение вне диапазона -5.0, 5.0 или b равен a. Приводим к ближайшему...")
    if b < -5:
        b = -5.0
    elif b > 5:
        b = 5.0

if a < b:
    print(f"[{a}, {b}] - Диапазон")

else:
    print(f"[{b}, {a}] - Диапазон")

while n != 0:
    num = float(input("Введите значение элемента массива от -5.0 до 5.0: "))
    if -5.0 > num or num > 5.0:
        print("Значение вне диапазона -5.0, 5.0. Приводим к ближайшему...")
        if num < -5:
            num = -5.0
        elif num > 5:
            num = 5.0
    arr.append(num)
    n = n - 1
print("Исходный массив:", arr)

# Шаг 3: Нахождение номера максимального по модулю элемента
abs_num = [abs(x) for x in arr]
max_abs_ind = abs_num.index(max(abs_num))
print(f"Номер максимального по модулю: {max_abs_ind}")
# Шаг 4: Вычисляем сумму элементов массива, которые находятся после первого положительного.
n = len(arr)
nummer = arr
count = 0
flag = 1
summer = 0
while flag:
    if nummer[count] > 0:
        flag = 0
        summer = sum(nummer)
        break
    else:
        nummer.pop(0)
        count += 1
print(f"Сумма элементов массива, которые находятся после первого положительного: {summer}")

# Шаг 5: Упорядочиваем элементы массива, чтобы сначала располагались все элементы, целая часть которых лежит в интервале [а, b], а потом — все остальные.

nummer = arr
in_range = [x for x in nummer if a <= x <= b]

out_range = [x for x in nummer if x not in in_range]

nummer = sorted(in_range, reverse=True) + sorted(out_range, reverse=True)
print(f"Упорядоченный массив: {nummer}")