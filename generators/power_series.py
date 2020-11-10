def power(base, exp):
    if exp == 1:
        yield base
    if exp != 1:
        yield base * power(base, exp - 1)


oa = power(5, 2)
for i in oa:
    print(i)

# def fact(n):
#     if n == 0:
#         yield 1
#     if n == 1:
#         yield 1
#     yield n * fact(n - 1)
#
#
# A = fact(5)
# for i in A:
#     print(fact(i))


# def fn(m, n):
#     i = m
#     while i < n:
#         yield i
#         i += 1
#
#
# var = fn(1, 10)
# for i in var:
#     print(i)
