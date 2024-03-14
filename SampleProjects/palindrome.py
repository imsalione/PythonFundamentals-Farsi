my_str = input('Enter a string word: ')

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")