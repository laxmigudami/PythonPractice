n = int(input("enter the number:"))
flag = 0
for i in range(1, n // 2 + 1):
    if n == i * i:
        flag = 1
        break
if flag == 1:
    print("number is a perfect square")
else:
    print("number is not a perfact square")

