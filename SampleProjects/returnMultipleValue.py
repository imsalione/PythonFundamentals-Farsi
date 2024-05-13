def name():
    return "saleh", "alireza"

# print the tuple with the returned values
print(name())

print("-------------------------------\n")

# get the individual items
name1, name2 = name()
print(name1, name2)

print('-------------------------------\n')

# loop the function to return separated values
for x in name():
    print(x)

print('-------------------------------\n')
    
# using dictionary
def name2():
    n1 = "saleh"
    n2 = "alireza"
    
    return {1 :n1, 2 :n2}

name = name2()
print(name)