rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()
    
print("-------------------------------------")
    
rows2 = int(input("Enter number of rows: "))

for i in range(rows2):
    for j in range(i + 1):
        print(j+1, end=" ")
    print()
    
print("-------------------------------------")

rows3 = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
        
    ascii_value += 1
    print()