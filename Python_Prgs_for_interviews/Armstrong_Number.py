#armstrong number is such that the sum of the cube of its all digits is equal to the same number
#ex 153
#1**3 + 5**3 + 3**3 = 153

num = int(input("enter the number:"))
sum = 0
temp = num
while temp > 0:
    c = temp % 10
    sum += c**3
    temp = temp // 10
if sum == num:
    print("its armstrong number")
else:
    print("not a armstrong number")