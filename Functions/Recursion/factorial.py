def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


n = int(input("Enter a number:"))
if n < 0:
    print("sorry, factorial does not exist for negative numbers")
else:

    print(" the factorial of", n, "is", fact(n))
