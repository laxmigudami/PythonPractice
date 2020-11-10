def fact(n):
    if n in [0, 1]:
        return 1
    return n * fact(n - 1)


class FactorialSeries:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __iter__(self):
        self.m = 0
        return self

    def __next__(self):
        if self.m <= self.n:
            res = fact(self.m)
            self.m += 1
            return res
        else:
            raise StopIteration


a = FactorialSeries(0, 10)
for i in a:
    print(i)
