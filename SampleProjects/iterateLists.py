import itertools

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

# using zip (loop untile short loop stops)
for i, j in zip(list1, list2):
    print(i, j)

print('----------------------------')
    
# using itertools (loop until the longer list stops)
for i, j in itertools.zip_longest(list1, list2):
    print(i, j)