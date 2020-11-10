# def bubble(a):
#     n = len(a)
#     for passno in range(1, n):
#         for i in range(0, n - 1):
#             if a[i] > a[i + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#     return a
#
#
# print(bubble([6, 7, 3, 4, 2, 5, 1]))

def bubble(a, passno=1):
    n = len(a)
    if passno == n:
        return a
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        return bubble(a, passno + 1)
print(bubble([6, 7, 3, 4, 2, 5, 1]))
