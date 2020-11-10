# # split()
# # var1, var2 = input("enter the msg has to be conveyed").split()
# # in split function we can mention variable to be seperated by , # etc.,
#
# a, b = input("enter the values:").split(",")
# print("value of a is:", a)
# print("value of a is:", b)
#
# # multiple inputs in Python using input
# x, y = input("Enter First Name: "), input("Enter Last Name: ")
# print("First Name is: ", x)
# print("Second Name is: ", y)

# # map() #map (fun, iter)
# # variable 1, variable 2, variable 3 = map(int,input().split())
#
# x, y = map(float, input("Enter two values: ").split())  # it will map int, float etc data types to all values
# print("First Number is: ", x)
# print("Second Number is: ", y)

# List Comprehension
# x, y=[x for x in input("Enter two value: ").split()]

# multiple inputs in Python using list comprehension

x, y = [x for x in input("enter the name and age:").split(",")]
print("your name is: ", x)
print("your age is: ", y)
