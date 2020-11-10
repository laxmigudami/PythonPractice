# fibonacci series has numbers in which each number is the sum of two preceding numbers
# 0 1 1 2 3 5 8 13 21 34 ...
a = int(input("enter the first number"))
# b = int(input("enter the second number"))
n = int(input("enter the number of elements"))

b = a+1
print(a, b, end=" ")
while n-2:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n = n-1

