n = int(input('Введите количество чисел: '))
tup = tuple(int(input('Введите элементы: ')) for i in range(n))
number = int(input('Введите число: '))

first = -1
second = -1

for i in range(len(tup)):
    if tup[i] == number:
        if first == -1:
            first = i
        else:
            second = i
            break

if first == -1:
    print(())

elif second != -1:
    print(tup[first:second + 1])
else:
    print(tup[first:])
