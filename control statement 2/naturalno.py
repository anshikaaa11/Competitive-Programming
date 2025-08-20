n = int(input("Enter a positive integer N: "))
if n < 1:
    print("Please enter a positive integer:")
else:
    while n >= 1:
        print(n, end=" ")
        n -= 1
    print()