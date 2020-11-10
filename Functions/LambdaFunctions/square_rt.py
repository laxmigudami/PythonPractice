#lambda functions in the python are also called Anonymous Functions(functions without name)
def sqaure(a):
    return a*a
res = sqaure(6)
print(res)


# syntax lambda argument(s) : expression
f = lambda a: a*a
res = f(6)
print(res)
print(f(10))

# f= function object that accepts and stores the result of the expression
# lambda = keyword
# a = argument
# a*a = one line expression

# lambda functions are used for creatig small, one line anonymous functions without
# much effort
# lambda functions are very useful when using with the map() and filter()
