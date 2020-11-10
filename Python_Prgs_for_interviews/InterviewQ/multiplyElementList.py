# 6.	Get the given number from a list and multiply it with other numbers in the list and store it in another list.
# Eg:[1,2,3,4,5]  num = 3  o/p : [3,6,12,15]

# l = [1,2,3,4,5]
# num= int(input("enter the number from the list "))
# for i in l:
#     new_list =

def mul_list(l, n):
    list_ = []
    l = l.remove(n)
    for i in l:
        list_.append(i * n)
    print(list_)


mul_list([1, 2, 3, 4, 5], 3)
