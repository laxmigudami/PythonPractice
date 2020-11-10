from operator import *
from decimal import *
from random import *
from string import *
from math import *


# Since Python provides a lot of built-in modules, it is advisable to use built-in modules rather than user-created modules to perform basic operations

a,b = 10,20
# product of a, b
print(mul(a,b))
# prints True if the value of a is greater than b else false
print(gt(a,b))
# prints the remainder when the value of a is divided by b
print(mod(a,b))
# concatenates and prints the given two strings
print(concat("FACE", "Prep"))


a,b =10,3
c= a / b
print(c)
print(Decimal(c))
# prints the complete decimal value of c


print(randint(10,20))
# prints the random nmber btw the given numbers
list1 = [30,23,45,16,89,56]
print(choice(list1))
# prints a random element from the given iterator
print(uniform(10,20))
# prints the random float number between two given values



print(capwords("fACE prep"))
# capitalizes the first letter of each words
print(ascii_letters)
# prints all lowercase and uppercase letters


print(sqrt(16))
# prints the square root of the value 16 in the form of a floating point value
print(factorial(5))
# prints the factorial of value 5