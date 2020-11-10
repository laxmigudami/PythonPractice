n = int(input("enter the number:"))
s = 0
m = n
while n != 0:
    ld = n % 10
    n = n // 10
    fact = 1
    for i in range(1, ld + 1):
        fact = fact * i
    s = s + fact
    print(s)

if m == s:
    print("strong number")
else:
    print("not strong number")
