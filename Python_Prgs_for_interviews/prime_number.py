# a prime number has only two factors, which is 1 and the number itself. we will make
# a prg to check if a number is a prime number or not




num = int(input("enter the number:"))
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 1:
    print("not prime number")
else:
    print("prime number")


