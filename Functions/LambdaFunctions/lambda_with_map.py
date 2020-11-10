# def func(a):
#     return l
#
#
# list1 = ["FACE Prop", "Python"]
# res = map(func, list1)
# print(list(res))

# using lambda function

# list1 = ["FACE Prop", "Python"]
# res = map(lambda a: len(a), list1)
# print(list(res))en(a)
# lambda will return the boolean value if we are using condition in the expression

list2 = [12, 13, 14, 66, 76, 79]
f = lambda a: a%2 == 0 #lambda exression should return a single value, if we are using multiple expressions then it will gives name error

f(2)
res = list(filter(lambda a: a % 2 == 0, list2)) #whatever the function we write inside the filter it should always return boolean values
print(res)

res = list(map(lambda a: a*a, list2))
print(res)
