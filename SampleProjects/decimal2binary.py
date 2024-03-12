def dec2binary(n):
    if n > 1:
        dec2binary(n//2)
    print(n % 2, end='')
    
dec = int(input("Enter a number: "))

dec2binary(dec)

print()