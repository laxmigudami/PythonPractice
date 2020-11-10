#split() --- helps us to get the multiple inputs from the user and assign them to the respective variables in one line.
#this function breaks the input by the specified seperator
#vae1, var2 = input("enter the values").split()
a,b = input("enter values: ").split()
print("first number is:", a)
print("second number is:", b)
a,b = input("enter values: ").split(",")
print("first number is:", a)
print("second number is:", b)

# input()
x, y = input("enter first name:"), input("enter the last name:")
 # map()
 # var1, var2, var3 = map(int/str, input().split())

 # list comprehension
 # x, y = [x for x in input("enter the vaue:").split()]