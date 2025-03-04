n = int(input('Введите количество чисел: '))
tup = tuple(int(input('Введите элементы: ')) for i in range(n))
el = int(input('Введите эелемент, который хотите удалить: '))

if el in tup:
    index = tup.index(el)
else:
    index = el

if index > n:
    prime = tuple(el for el in tup)
    print(prime)
else:
    print(tup[:index]+tup[index+1:])
