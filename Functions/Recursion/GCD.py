def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# main() function
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
GCD = gcd(a, b)
print("gcd is :", GCD)

# the end condition is mandatory in the recurssion if end condition is not provided
# the recursion will throw an error is recursive error
