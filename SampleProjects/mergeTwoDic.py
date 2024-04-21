dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

print(dict_1 | dict_2)

dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)