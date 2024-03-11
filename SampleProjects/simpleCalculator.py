def calculate(x, y):
    if choice == '1':
        return x + y
    if choice == '2':
        return x - y
    if choice == '3':
        return x * y
    if choice == '4':
        return x / y
    
print("Select operation.")
print("  1.Add")
print("  2.Subtract")
print("  3.Multiply")
print("  4.Divide")
           
while True:
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        if choice == '1':
            print(num1, "+", num2, "=", calculate(num1, num2)) 
            
        elif choice == '2':
            print(num1, "-", num2, "=", calculate(num1, num2))  
            
        elif choice == '3':
            print(num1, "*", num2, "=", calculate(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", calculate(num1, num2)) 
            
        next_calculation = input("Let's do next calculaton? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")