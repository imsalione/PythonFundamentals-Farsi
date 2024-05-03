list1 = [1, 'a']
list2 = [3, 4, 5]

list_joined = list1 + list2

print(list_joined)

print('--------------------------')

list3 = [1, 'a']
list4 = range(3, 6)

list_joined = [*list3, *list4]
print(list_joined)

print('--------------------------')

list5 = [1, 'a']
list6 = [3, 4, 5]

list_joined = list(set(list5 + list6))
print(list_joined)

print('--------------------------')

list7 = [1, 'a']
list8 = [1, 2, 3]

list8.extend(list7)
print(list8)