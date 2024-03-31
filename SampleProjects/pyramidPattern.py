rows = int(input("1) Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()
print()
    
print("-------------------------------------\n")
    
rows2 = int(input("2) Enter number of rows: "))

for i in range(rows2):
    for j in range(i + 1):
        print(j+1, end=" ")
    print()
print()
    
print("-------------------------------------\n")

rows3 = int(input("3) nter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
        
    ascii_value += 1
    print()
print()
    
print("-------------------------------------\n")

rows4 = int(input("4) Enter number of rows: "))

for i in range(rows4, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
        
    print()
print()

print("-------------------------------------\n")

rows5 = int(input("5) Enter number of rows: "))

for i in range(rows5, 0, -1):
    for j in range(1, i+i):
        print(j, end=" ")
        
    print()
print()

print("-------------------------------------\n")

rows6 = int(input("6) Enter number of rows: "))

k = 0

for i in range(1, rows6 + 1):
    for space in range(1, (rows6 - i) + 1):
        print(end="  ")
        
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
        
    k = 0
    print()
print()

print("-------------------------------------\n")

rows7 = int(input("7) Enter number of rows: "))

k = 0
count = 0
count1 = 0

for i in range(1, rows7+1):
    for space in range(1, (rows7 - i) + 1):
        print("  ", end="")
        count += 1
        
    while k != ((2*i)-1):
        if count <= rows7 - 1:
            print(i + k, end=" ")
            count += 1
            
        else:
            count1 += 1
            print(i+k-(2*count1), end=" ")
        k += 1
        
    count1 = count = k = 0
    print()
print()

print("-------------------------------------\n")

rows8 = int(input("8) Enter number of rows: "))

for i in range(rows8, 1, -1):
    for space in range(0, rows8 - i):
        print("  ", end="")
    for j in range(i, 2 * i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
print()

print("-------------------------------------\n")

rows9 = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows9 + 1):
    for space in range(1, rows9-i+1):
        print(" ", end="")
    for j in range(0, i):
        if j == 0 or i == 0:
            coef = 1
        else:
            coef = coef * (i - j) // j
        print(coef, end=" ")
    print()
print()