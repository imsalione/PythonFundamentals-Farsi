terms = 10
# terms = int(input("Enter number of terms: "))


result = list(map(lambda x: 2 ** x, range(terms)))

print(result)

print("The total terms are:", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])