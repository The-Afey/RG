from random import randint

string = int(input('Введите количество строк матрицы: '))
colum = int(input('Введите количество столбцов матрицы: '))

matrix = []
for i in range(colum):
    row = []
    for j in range(string):
        row.append(randint(0, 255))
    matrix.append(row)

count = 0
for i in range(colum):
    for j in range(string):
        count += matrix[i][j]
medium = count / (string*colum)
print(f'{medium = :.4f}')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end ='\t', sep=' ' )
    print()


for i in range(colum):
    for j in range(string):
        if matrix[i][j] > medium:
            matrix[i][j] = 255
        else:
            matrix[i][j] = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end ='\t', sep=' ' )
    print()