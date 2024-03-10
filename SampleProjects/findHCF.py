def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hfc = i
    return hfc

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("The H.C.F is", compute_hcf(num1, num2))