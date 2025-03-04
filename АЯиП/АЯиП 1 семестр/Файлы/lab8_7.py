from math import trunc

n = int(input('Введите начальное значение\n'))
h = float(input('Введите шаг\n'))
nmax = float(input('Введите конечное значение\n'))
nx = trunc((nmax - n) / h + 1e-6) + 1

z = 0
for x in range(0, nx+1):
    if x <= 0.5:
        for n in range(1, 21):
            z += n/(n+1)
        y = x/2 * z
    else:
        for n in range(1, 9):
            z += x**n/n
        y = z

print(y)
