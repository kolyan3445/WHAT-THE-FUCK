import turtle
import math

# Настройка окна и черепахи
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.setworldcoordinates(-10, -10, 10, 10)
screen.title("Laba-6")
t = turtle.Turtle()
t.speed(0)
t.penup()

# Функция для вычисления y в зависимости от x
def calculate_y(x):
    if x < -6:
        return -2 * x - 14
    elif -6 <= x <= -2:
        return -2 + math.sqrt(2 ** 2 - (x + 4) ** 2)
    elif -2 < x < 2:
        return math.log2(2 + x)
    elif 2 <= x < 4:
        return math.sqrt(1 ** 2 - (x - 3) ** 2)
    else:
        return 0

# Рисуем оси координат
t.pencolor("blue")
t.goto(-10, 0)
t.pendown()
t.goto(10, 0)
t.penup()
t.goto(0, -10)
t.pendown()
t.goto(0, 10)
t.penup()

# Подписываем оси X и Y
t.goto(9.5, -0.5)
t.write("X", align="center", font=("Arial", 12, "normal"))
t.goto(-0.5, 9.5)
t.write("Y", align="center", font=("Arial", 12, "normal"))

# Градуировка оси X
for x in range(-10, 11):
    t.goto(x, 0)
    t.pendown()
    t.goto(x, -0.2)
    t.penup()
    if x != 0:
        t.goto(x, -0.5)
        t.write(str(x), align="center", font=("Arial", 8, "normal"))

# Градуировка оси Y
for y in range(-10, 11):
    t.goto(0, y)
    t.pendown()
    t.goto(-0.2, y)
    t.penup()
    if y != 0:
        t.goto(-0.5, y)
        t.write(str(y), align="right", font=("Arial", 8, "normal"))

# Отмечаем ноль на оси X
t.goto(0, 0)
t.dot(8, "red")  # Красная точка в центре
t.goto(0.2, -0.5)
t.write("0", align="center", font=("Arial", 8, "normal"))



# Рисуем график функции
t.pencolor("green")
t.pensize(2)  # Увеличиваем толщину линии
x = -10
t.goto(x, calculate_y(x))
t.pendown()
while x <= 10:
    y = calculate_y(x)
    t.goto(x, y)
    x += 0.1

# Завершение
t.hideturtle()
screen.mainloop()