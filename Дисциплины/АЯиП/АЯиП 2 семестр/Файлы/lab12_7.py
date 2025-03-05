sente = input('Введите предложение (на английском): ').split(' ')
alfabet = {'e', 'y', 'u', 'i', 'o', 'a', 'E', 'Y', 'U', 'I', 'O', 'A'}

result = set()
for i in sente:
    for j in i:
        if j in alfabet:
            result.add(j)

print(*result)