#inplace operator functions
# iadd(a,b)----> performs the addition of a and b then assigns this result to a
# assigning doesnot takes place if a and b are of immutable data types like numbers, strings, tuples
# a+=b
from operator import *
num1, num2 = 5, 3
print(iadd(num1,num2))
print(num1)

list1 = ['FACE']
list2 = ['Prep']
print(iadd(list1, list2))
print(list1)


num1, num2 = 5, 3
print(isub(num1, num2))
print(num1)

num1, num2 = 5, 3
print(imul(num1, num2))
print(num1)

num1, num2 = 5, 3
print(itruediv(num1, num2)) #----> num1/=num2

num1, num2 = 5, 3
print(imod(num1, num2))  #-----> num1%=num2

list1 = ['FACE']
list2 = ['Prep']
print(iconcat(list1, list2))
print(list1)

# inplace operators performs the computation and assignment in the single statement
#  post computation the value will be assigned to the first operand
# data types of the values must be mutable type i e other than the string, number and tuple
















