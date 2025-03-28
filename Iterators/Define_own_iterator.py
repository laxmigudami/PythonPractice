# iterator to multiply numbers less than n with 2
class Numbers:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 * self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = Numbers(8)
for i in a:
    print(i)
