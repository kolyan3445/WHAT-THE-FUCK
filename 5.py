#-------------ЧАСТЬ 1-------------
from math import *

# Чтение значения x из файла
with open('input.txt', 'r') as file:
    x = float(file.readline().strip())

# Вычисление значений z1 и z2
z1 = (sin(4 * x)) / (1 + cos(4 * x)) * (cos(2 * x) / (1 + cos(2 * x)))
print(x, z1)
z2 = cos((3/2) * pi - x) / (sin(3/2) * pi - x)
print(x, z2)


# Запись результатов в файл
with open('output.txt', 'w') as file:
    file.write("{0:.2f} {1:.4f}\n".format(x, z1))
    file.write("{0:.2f} {1:.4f}\n".format(x, z2))

"""
#-------------ЧАСТЬ 2-------------
# Функция для чтения входных данных из файла
def read_input(filename):
    with open(filename, 'r') as file:

        arr = [float(x.replace('\n', '', 1)) for x in file.readlines()]
        n = arr[0]  # Чтение количества элементов
        a = arr[1]  # Чтение числа a
        b = arr[2]  # Чтение числа b

        arr.remove(n)
        arr.remove(a)
        arr.remove(b)
    return n, a, b, arr

# Функция для записи результатов в файл
def write_output(filename, arr_norm, a, b, max_abs_ind, nummer, summer):
    with open(filename, 'w') as file:
        file.write("Исходный массив:\n")
        file.write(str(arr_norm).replace('[', '').replace(']', '').replace(',', '') + "\n")
        file.write(f"Значение a: {a}\n")
        file.write(f"Значение b: {b}\n")
        file.write(f"Номер максимального по модулю: {max_abs_ind}\n")
        file.write("Упорядоченный массив:\n")
        file.write(str(nummer).replace('[', '').replace(']', '').replace(',', '') + "\n")
        file.write(f"Сумма элементов массива, которые находятся после первого положительного: {summer}\n")
n, a, b, arr = read_input("input2.txt")
# Основная программа
def main(n, a, b, arr):
    # Чтение входных данных
    orig_arr = arr
    #print(orig_arr)

        # Шаг 1: Запрос количества элементов массива (не более 30)
    if n > 30:
        print("Количество элементов не должно превышать 30. Установлено значение 30.")
        n = 30

    # Шаг 2: Создание массива с убывающими случайными значениями в диапазоне [-5.0, 5.0]

    if -5.0 > a or a > 5.0:
        print("Значение вне диапазона -5.0, 5.0. Приводим к ближайшему...")
        if a < -5:
            a = -5.0
        elif a > 5:
            a = 5.0

    if (-5.0 > b or b > 5.0) and b != a:
        print("Значение вне диапазона -5.0, 5.0 или b равен a. Приводим к ближайшему...")
        if b < -5:
            b = -5.0
        elif b > 5:
            b = 5.0

    # Шаг 3: Нахождение номера максимального по модулю элемента
    abs_num = [abs(x) for x in arr]
    max_abs_ind = abs_num.index(max(abs_num)) + 1

    # Шаг 4: Вычисляем сумму элементов массива, которые находятся после первого положительного.
    n = len(arr)
    flag = 1
    summer = 0
    nummer = arr
    arr = str(arr).replace('[', '').replace(']', '').replace(',', '')
    #print(arr)
    while flag:
        if nummer[0] > 0:
            flag = 0
            nummer.pop(0)
            summer = sum(nummer)
            break
        else:
            #print(nummer)
            nummer.pop(0)

    # Шаг 5: Упорядочиваем элементы массива, чтобы сначала располагались все элементы, целая часть которых лежит в интервале [а, b], а потом — все остальные.
    sorted_arr = [float(x) for x in arr.split()]
    in_range = [x for x in sorted_arr if a <= x <= b]

    out_range = [x for x in sorted_arr if x not in in_range]

    sorted_arr = sorted(in_range, reverse=True) + sorted(out_range, reverse=True)

    # Запись результатов в файл
    write_output("output2.txt", arr, a, b, max_abs_ind, sorted_arr, summer)

main(n, a, b, arr)
"""