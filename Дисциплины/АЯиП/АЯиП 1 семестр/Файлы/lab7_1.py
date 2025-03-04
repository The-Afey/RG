# Программа lab7_1
# Тема: Цикл с предусловием.
# Задание 6_3 табулирование реализовать циклом while.
# Программист: Гукало Д.Г. гр.445
# Проверил: Бурмистров А.С.
# Дата написания: 13.11.2024
# Переменные:
# n, h, nmax - входные данные
# summa, product, y - выводимые значения
# x - параметр цикла


from math import *


def func(x):
    if abs(x) <= 1:
        return abs(x)
    elif 1 < abs(x) <= 2:
        return x**2
    else:
        return 4


n = int(input('Введите начальное значение\n'))
h = float(input('Введите шаг\n'))
nmax = float(input('Введите конечное значение\n'))

summa = 0
product = 1
x = n
while x <= nmax:
    y = func(x)
    print('x = %.1f \t y = %.2f' % (x, y))
    x += h
    summa += y
    product *= y


print(f'сумма = {summa}  \t произведение = {product}')
