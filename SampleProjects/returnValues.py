def name():
    return "saleh", "elham"

print(name())

name_1, name_2 = name()
print(name_1, name_2)

print('-------------------------')

def name():
    n1 = 'saleh'
    n2 = 'elham'
    
    return {1:n1, 2:n2}

names = name()
print(names)