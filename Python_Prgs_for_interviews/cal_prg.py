def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


def si(p, r, t):
    return (p * r * t) / 100

def ci(P, R, T):
    return P * pow((1 + R/100), T)


def sqr(num):
    return num**2

def sqrt(num):
    return num**0.5
print(sqrt(64))