word = input("Enter a word: ")
my_list = []

for i in word:
    my_list += i

if not my_list:
    print("the list is empty")
else:
    print("the list is not empty:",my_list)