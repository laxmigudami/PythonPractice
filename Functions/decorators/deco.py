import time


def time_calc(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, *kwargs)
        end= time.time()
        print("total time taken is:", end-start)
    return inner
@time_calc
def cube(n):
    for i in range(n):
        res = i**3
cube(1000)

@time_calc
def sqare(n):
    for i in range(n):
        res = i**2
sqare(30000)

