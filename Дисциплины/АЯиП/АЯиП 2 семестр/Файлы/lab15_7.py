# string = 'python'

# dictionary = {k: string.count(k) for k in set(string)}

# print(dictionary)


string = 'python'

dictionary = {}

for k in set(string):
    count = string.count(k)
    dictionary[k] = count

print(dictionary)
