def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


class FibonacciSeries:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.m = 1
        return self

    def __next__(self):
        if self.m <= self.n:
            res = fibo(self.m)
            self.m += 1
            return res
        else:
            raise StopIteration


a = FibonacciSeries(15)
for i in a:
    print(i)
