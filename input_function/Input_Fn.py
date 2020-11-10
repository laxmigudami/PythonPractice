#to take the single input from the user
# input() is used it always convert the inputed data into strings
# so if we want any intended type of data we can reconvert it  by type casting

a = input("enter the value:")
print(type(a)) #<class 'str>
a = int(input("enter the value:"))
print(type(a))