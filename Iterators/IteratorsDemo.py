# iterators in the python are used to iterate through a sequence without knowing the index value of the elements
# this sequence is called as iterable and python has inbuilt iterable objects like lists, strings, tuples, dict, set
#  help save resources and make the code look cleaner
list = [1, 2, 3, 4, 5]
a = iter(list)
print(a)
# print(a.__next__())
# # print(a.__next__())
# print(next(a))
print(next(a))
