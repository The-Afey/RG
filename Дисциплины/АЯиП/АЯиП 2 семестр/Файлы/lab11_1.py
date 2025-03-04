n = int(input('Введите количество чисел: '))
tup = tuple(int(input("Введите элементы: ")) for i in range(n))
number = int(input('Введите число: '))
count = 0
for i in range(len(tup)):
    for j in range(i, len(tup)):
        if tup[i] * tup[j] == number:
            count += 1
if count > 0:
    print('Да')
else:
    print('Нет')
