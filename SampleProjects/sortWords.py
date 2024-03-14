my_str = "Hello this is an Example With cased lettters"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are: ")

for word in words:
    print(word)