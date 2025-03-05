set1 = set(input('Введите первое множество: '))
set2 = set(input('Введите второе множество: '))
set3 = set(input('Введите третье множество: '))
set4 = set(input('Введите четвёртое множество: '))

result1 = set1 | set2 | set3
result2 = set1 & set4
final_result = result1 - result2

print(final_result)