n = int(input("enter the number:"))
i = 1
fact = 1
flag = 1
while fact <= n:
    if fact == n:
        flag = 1
        break
    fact = fact * i
    i += 1
if flag == 1:
    print("perfect factorial")
else:

    print("not perfect factorial")




