def find_max(list):
    max_el = list[0]
    el_index = 0
    for i in range(len(list)):
        if list[i] > max_el:
            max_el = list[i]
            el_index = i
    return max_el, el_index


matrix = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(int(input('Введите элементы двумерной матрицы: ')))
    matrix.append(row)

print('Введённая матрицца:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t', sep='')
    print()

real_max = 0
string = 0
for j in range(2):
    mx_matrix, index_matrix = find_max(matrix[j])
    if real_max < mx_matrix:
        real_max = mx_matrix
        string = j
    print(
        f'В строке матрицы {j+1} максимальный элемент равен {mx_matrix}, его номером {index_matrix+1}')
print(
    f'Максимальный элемент матрицы расположен в строке номер {string+1} и равен {real_max}')
