# syntax  array_name = array('datatype', [array_elements])
from array import *

array_name = array('i', [2, 3, 4, 5, 6])
print(array_name)
array_name.append(40)
for x in array_name:
    print(x, end=" ")
print(array_name)
array_name.pop(0)  # deleted by specifying the index value
for x in array_name:
    print(x, end=' ')
#
array_name.remove(40)
print(array_name)
