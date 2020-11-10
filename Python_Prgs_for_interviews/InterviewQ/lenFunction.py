# Len function without len inbuilt function

def _len(interable):
    count = 0
    for char in interable:
        count += 1
    return count


print(_len("laxmigudami"))
print(_len([1, 2, 3, 4, 5]))
