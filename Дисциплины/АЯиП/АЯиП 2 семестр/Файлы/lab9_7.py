# Lab9_7
from random import randint
array = []
for i in range(20):
    array.append(randint(-10, 10))
minus = []
plus = []
for i in range(len(array)):
    if array[i] >= 0:
        plus.append((array[i]))
    else:
        minus.append(array[i])

print(array)
print(plus, minus)
