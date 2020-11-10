# Write a program to reverse a string without using any inbuilt functions.

def reverse_str(string):
    temp = []
    print(string)
    print(len(string))
    for i in range(len(string) - 1, -1, -1):
        temp.append(string[i])
    return ''.join(temp)


print(reverse_str("laxmi gudami"))
