#Пример 9_3
#Поиск минимального элемента
#в массиве и его индекса и макс. эл-та
a = list(map(float, input().split()))
print(*a)

#поиск макисмума
amax = a[0]   #amax = -float('inf') 
for el in a:
    if el > amax:
        amax = el
print('макс. эл-т', amax)

#поиск минимума и его индекса
amin = a[0] #amin = float('inf')
imin = 0
for i in range(1, len(a)):
    if a[i] < amin:
        amin = a[i]
        imin = i
print('мин. эл-т', amin, 'его индекс', imin)         



