# class EvenNumbers:
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < 10:
#             n = self.n
#             self.n += 2
#             return n
#         else:
#             raise StopIteration
#
#
# a = EvenNumbers()
# for i in a:
#     print(i)


# class EvenNumbers:
#     def __init__(self, num):
#         self.num = num
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < self.num:
#             n = self.n
#             self.n += 2
#             return n
#         else:
#             raise StopIteration
#
#
# a = EvenNumbers(100)
# for i in a:
#     print(i)

class evenNumbers:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.num:
            n = self.n
            self.n += 2
            return n
        else:
            raise StopIteration


a = evenNumbers(100)
for i in a:
    print(i)
