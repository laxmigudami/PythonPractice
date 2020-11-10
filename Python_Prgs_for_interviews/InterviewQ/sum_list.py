# def list_sum(lst):
#     return [sum(i) for i in zip(*lst)]
#
#
# print(list_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# 5.	WAP to print the sum of: [[1,2,3],[4,5,6],[7,8,9]]
# a.	Whole list  45
# b.	Nested lists  [6,15,24]


# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = []
# b = 0
# for i in l:
#     s = 0
#     for x in i:
#         s += x
#         b += x
#     a.append(s)
# print(a)
# print(b)


# def nested_sum(L):
#     sum = 0
#     for i in range(len(L)):
#         if len(L[i]) > 1:
#             sum = sum + nested_sum(L[i])
#         else:
#             sum = sum + L[i]
#     return sum
# nested_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



def nested_sum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total
print(nested_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))     