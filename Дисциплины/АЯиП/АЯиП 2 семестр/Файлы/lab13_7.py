from random import randint


def create_matrix(dimension):
    matrix = []
    for _ in range(dimension):
        row = []
        for _ in range(dimension):
            row.append(randint(-100, 100))
        matrix.append(row)
    return matrix


def show_matrix(dimension, matrix):
    for i in range(dimension):
        for j in range(dimension):
            print(matrix[i][j], end='\t', sep='')
        print()


def find_max(list):
    max_el = list[0]
    el_index = 0
    for i in range(len(list)):
        if list[i] > max_el:
            max_el = list[i]
            el_index = i
    return max_el, el_index


dimension = 2


matrix = create_matrix(dimension)
print('Исходная матрица')
show_matrix(dimension, matrix)


real_max = 0
string = 0
for j in range(len(matrix)):
    mx_matrix, index_matrix = find_max(matrix[j])
    if real_max < mx_matrix:
        real_max = mx_matrix
        string = j
    print(
        f'В строке матрицы {j+1} максимальный элемент равен {mx_matrix}, его номер {index_matrix+1}')
print(
    f'Максимальный элемент матрицы расположен в строке номер {string+1} и равен {real_max}')
