while True:
    try:
        num = int(input("Enter a number (More than 9): "))
        reversed_num = 0
        
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
            
        print("Reversed Number: " + str(reversed_num))
        break
        
    except ValueError:
        print("Enter Valid Number!")