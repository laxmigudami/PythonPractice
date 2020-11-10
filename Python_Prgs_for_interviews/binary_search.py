def binary_search(x, a):
    n = len(a)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif x > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


pos = binary_search(2, [1, 2, 3, 5, 6, 7, 8])
if pos ==  -1:
    print("the element not found")
else:
    print("element is found")
