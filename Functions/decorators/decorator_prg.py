# write a decorator that returns only positive values of subtraction
def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper

@positive
def sub(a,b):
    return a - b

print(sub(12, 56))
