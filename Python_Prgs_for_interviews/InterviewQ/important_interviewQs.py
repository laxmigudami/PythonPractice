# Write a program to search for a character in a given string and return the corresponding index.
def search_character(string, key):
    for index, c, in enumerate(string):
        if c == key:
            print(f'character {c} is at index {index}')
search_character('hello world', 'w')

sentence = "python is a programming language"
# d = {'p':['python', 'programming'] , 'i': ['is'] , 'a': ['a'] , 'l' : ['language'] }

from collections import defaultdict
d = defaultdict(list)
words = sentence.split()
for word in words:
    d[word[0]].append(word)
# print(d)

# Write a to replace all the characters with - if the character occurs more than once in a string
my_string = "hellohai" #o/p should be '-e--o-ai

ss = set(my_string)
# get all the unique characters

for ch in ss:
    if my_string.count(ch) > 1:
        my_string = my_string.replace(ch, '-')
# print(my_string)

temp = ""
for i in my_string:
    if i not in temp:
        temp += i
    else:
        temp+= "-"
# print(temp)


# Write a function which takes a list of strings and integers.
# If the item is a string it should print as is and
# if the item is integer of float it should reverse it.

def spam(items):
    for item in items:
        if isinstance(item, str): #check the if the item is an instance of string
            print(item)
        else:
            temp = str(item)
            print(temp[::-1])
spam(['apple', 'yahoo', '1234', 100, 123.76, '26.23'])






