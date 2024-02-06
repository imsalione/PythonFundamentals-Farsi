import sys

while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print("The sum is: ", a + b)
        sys.exit()
    except ValueError:
        print("You shoud enter an integer number!")