def greet(name):
    print(name)


greet(name="laxmi")  # using keyword
greet("laxmi")  # using positional argument


def add(a, b):
    print(a + b)


add(1, 2)
add(a=1, b=2)
add(1, b=2)


# add(a=1, 2) not allowed positional argument should come first

def add(a, *, b):  # after star its keyword argument
    print(a + b)


add(1, b=2)


# what is difference btw arguments and parameters

def func(*args, **kwargs):  # accepts any number of arguments
    print(args)  # prints in the form tuple
    print(kwargs)  # stored in the form of dictionary


func(1, 2, 3, 4, a=15, b=12)

data = [1, 2, 3, 4]
func(*data)  # func(data[0], data[1], data[2], data[3])


# it unpacks the data and each element will be sent as  each argument

# if its dictionary
def spam(a, b):
    print(a, b)


d = {'a': 1, 'b': 2}
spam(**d)  # spam(a=1, b=2, c=3,d=4)



a= [1,2,3,4]
def spam(nums):
    nums.append(100)
    print(nums)
spam(a)
print(a)
# both nums and a is pointing to the same memory.  call by reference if its collection and mutable data
# if its single data type, it behaves like call by value
# so python is call by value as well as call by reference it depends on type of the data, its mutable or immutable
# or its none it depends on the object we are passing to the function.
a= (1,2,3,4)
def spam(nums):
    nums = nums + (1, 2, 3)
    print(nums)
spam(a)
print(a)


d= {'a': 1, 'b': 2}
def spam(nums):
    nums['a'] =10
    nums['b'] = 20
    print(nums)
spam(d)
print(d)
# here nums mutated the original dictionary
# difference between modules and scripts---module is imported


# lambda expressions
# inline expressions, mainly used in sorting
# these are ananymouse function means function without name

from collections import namedtuple
record = namedtuple("record", ['name', 'shares', 'price'])
print(record)
# it creates the class
#
