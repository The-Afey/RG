# Программа lab6_2
# Тема: Конечные суммы и произведения.
# Вычислить f.
# Программист: Гукало Д.Г. гр.445
# Проверил: Бурмистров А.С.
# Дата написания: 30.10.2024
# Переменные:
# k - входные данные
# f - вычисляемое значение
# i - параметр цикла


k = int(input('Введите число\n'))

if k % 2 == 0:
    l = 2
else:
    l = 1

y = (l * k)

f = 1
for i in range(2, y+1):
    f *= i

print(f)
