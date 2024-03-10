my_list = list(range(1, 101))

my_number = int(input("Enter a number: "))

result = list(filter(lambda x: (x % my_number == 0), my_list))

print(f"Numbers divisible by {my_number} are:", result)