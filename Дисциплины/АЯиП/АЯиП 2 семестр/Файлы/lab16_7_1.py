with open('lab16_7_1.txt', 'w') as file:
    from math import sin, pi
    elements = int(input('Введите количество элементов: '))
    for i in range(1, elements+1):
        result = ((i+1)**2)*sin((i*pi)/10)
        file.write(f'{result}\n')
    file.close()


with open('lab16_7_1.txt') as file:
    count = 0
    for i in file.readlines():
        if float(i.strip()) > 0:
            count += 1
print(count)
