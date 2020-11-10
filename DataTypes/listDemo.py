list1 =[ 20,29,39,45.2, "python", [1,2,3,4]]
#elements in the list can be accessed by using index operator[]


print(list1[0])

print(list1[4][1]) #nested indices
# negative indexing
print(list1[-1])
print(list1[-1][-3])

# accessing range of elements at a time #slicing unsing the slicing operator :
print(list1[0:1])
print(list1[0:5])  #here 1st index will be inclusive and last index will be exclusive


# modify an element in the list
# mutable
list1[0]=12
print(list1)
list1[0:3]=[1,2,3]
print(list1)

# adding new elemnt to the list
# extend() ----> adding the several elemnt at list
# append() ---->adding one elemnt at al list
list1.append(18.1)
print(list1)
list1.extend([5,6])
print(list1)

# insert() ----> insert(index value, elemnt to be inserted)
# used whenever we want to insert the pertivular element in a perticular position
list1.insert(1,18.1)
print(list1)

list1[1:1]=["New Element", 3, 87.1]
print(list1)

# to delete the elemnts in the list
# del --->can delete one elemet, several element or entire list
del list1[1]
print(list1)

del list1[1:5]
print(list1)

# del list1
# print(list1)---->throws me an error NameError

list2=[1,2,3,4,5]
import operator
# cmp(list1,list2)
# list functions
# len(list1)
# max(list2)
# min(list2)

# built in methods

# pop() ---> removes last element
print(list1)
list1.pop()
print(list1)
# clear()---> removes all the ements in the list
# count() ---> returns the index of the element or the number of times an element is presennt
# reverse() ---> reverrses the ements of the li







