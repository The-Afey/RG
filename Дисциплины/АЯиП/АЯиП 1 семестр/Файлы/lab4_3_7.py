# Программа lab4_3_7
# Тема: Разработка разветвляющихся алгоритмов и программ
# Составить алгоритм и программу, которая определяет, принадлежит ли точка с
# некоторыми координатами (x, y) заштрихованной области, изображенной на рисунке.
# Программист: Гукало Д.Г. гр.445
# Проверил: Бурмистров А.С.
# Дата написания: 02.10.2024
# Переменные:
# x, y - входные данные

print('Введите исходные координаты (x,y)')
x = float(input())
y = float(input())

# эхо-печать исходных данных
print(f'Координаты точки ({x}, {y})')

if y < 0:
    if x**2 + y**2 <= 4:
        print('Точка принадлежит области')
    else:
        print('Точка не принадлежит области')
else:
    if y <= 2*abs(x) and y <= -2*abs(x) + 4:
        print('Точка принадлежит области')
    else:
        print('Точка не принадлежит области')
