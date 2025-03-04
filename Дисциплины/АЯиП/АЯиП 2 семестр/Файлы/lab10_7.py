
# ? Сформировать произвольную квадратную матрицу. Определить число повторений каждого из значений первой строки

size = int(input('Введите размерность квадратной матрицы: '))

matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input('Введите элементы матрицы: ')))
    matrix.append(row)

for i in matrix:
    print(*i)


for j in range(size):
    a = matrix[0][j]
    count = 0
    for k in range(size):
        for l in range(size):
            if a == matrix[k][l]:
                count += 1
    print(f'элемент {a} встретился {count} раз')
