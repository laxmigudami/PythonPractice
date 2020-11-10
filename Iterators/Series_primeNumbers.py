# def isprime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     for value in range(2, n+1):
#         if n % value == 0:
#             return False
#         return True


def check(n, div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            return False
        else:
            return check(n, div - 1)
    else:
        return 'True'


class PrimeSeries:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.m = 2
        return self

    def __next__(self):
        if self.m <= self.n:
            if check(self.m):
                res = self.m
                self.m += 1
                return res
            self.m += 1
        else:
            raise StopIteration


a = PrimeSeries(20)
for i in a:
    print(i)
