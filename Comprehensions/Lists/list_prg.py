import heapq
import string
import math

list = [1, 2, 3, 4, 5]

# square the numbers in the list using list compressions
list_evens = [num ** 2 for num in list]
print(list_evens)

# Returns a list containing all vowels in the given string
my_string = 'Hello world'
list_vowels = [char for char in my_string if char.lower() in ['a', 'e', 'i', 'u', 'o']]
print(list_vowels)

# list comprehensions --> its creating the iterable object from the list
# syntax---> [ expression for item in list]
# it can identify when it receives the string or tuple and iterates it like a list and gives the list

# if and else
l = ["even" if i % 2 == 0 else "odd" for i in range(20)]  # prg to find out odd and even number
print(l)

# nested if
# syntax----> [expression for item in list <condition1> <condition 2>]
# Example
new_list = [y for y in range(100) if y % 5 == 0 if y % 10 == 0]
print(new_list)

nums = [1, 2, 3, 8, 5]
sq_num = [num ** 2 for num in nums]
print(sq_num)


# Names starting with Vowels


def get_vowel_names(iterable):
    return [name for name in iterable if name[0].lower() in ['a', 'e', 'i', 'o', 'u']]


print(get_vowel_names(['Laura', 'Steve', 'Bill', 'James', 'Bob', 'Greig', 'Scott', 'Alex', 'Ive']))


# # Names starting with Vowels
# def get_vowel_names2(iterable):
#     return [name for name in iterable if name[0].startswith(tuple(['a', 'e', 'i', 'o', 'u']))]
#
#
# print(get_vowel_names2(['Laura', 'Steve', 'Bill', 'James', 'Bob', 'Greig', 'Scott', 'Alex', 'Ive']))


# raise to the power of index
def raise_power(iterable_):
    return [num ** index for index, num in enumerate(iterable_)]


print(raise_power([1, 2, 3, 4, 5, 6, 7]))

# list of even numbers between 1 to 50

even_number = [num for num in range(1, 51) if num % 2 == 0]
print(even_number)

# generating list of pi values
pi_list = [round(math.pi, n) for n in range(1, 6)]
print(pi_list)

# removing the duplicate items from the list
list_dup = [4, 5, 4, 6, 7, 8, 9, 2, 1, 4]
numbers = sorted(list_dup)
deduct_dup = [num for index, num in enumerate(numbers) if index == 0 or num != numbers[index - 1]]
print(deduct_dup)

# Prints the names if the first char of the item starts with any letter in the first half of the alphabet character
names = ['apple', 'yahoo', 'google', 'facebook', 'dropbox', 'instagram', 'twitter', 'microsoft', 'next']
first_half_alphabets = string.ascii_lowercase[:13]
first_half = [name.title() for name in names if name[0] in first_half_alphabets]
print(first_half)

# factorial using list comprehension
list_ = [1, 2, 3, 4, 5, 6, 7, 8]


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


fact_lst = [fact(item) for item in list_]
print(fact_lst)


# # Reverse firstname and lastname in the list using list comprehension


def reverse_names(name):
    fname, lname = name.split()
    return f'{lname.title()} {fname.title()}'


fullnames = ['steve jobs', 'bill gates', 'tim cook', 'johny ive']
rev_fname_lname = [reverse_names(name) for name in fullnames]
# print(rev_fname_lname)

# reverse difference
l = [1, 2, 3, 4, 5]
rev_difference = [n1 - n2 for n1, n2 in zip(l, l[::-1])]
# print(rev_difference)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

# Getting user names from password.txt
l = [line.split(":")[0].strip() for line in open("linuxdetails.txt") if not line.strip().startswith('#')]
# print(l)


# Getting only ip addresses from web server log. Also, find out how may times
# Each IP address is appears in the list and create a dictionary.
ip_address = [line.split(" ")[0] for line in open("access-log.txt")]
# print(ip_address)

# using normal dict
dd = {}
for item in ip_address:
    if item in dd:
        dd[item] += 1
    else:
        dd[item] = 1
print(dd)

# using default dict
from collections import defaultdict

d = defaultdict(int)
for item in ip_address:
    d[item] += 1
print(d)

# using counter object
from collections import Counter
# A Counter is a dict subclass for counting hashable objects.
# It is an unordered collection where elements are stored as dictionary keys
# and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts
c = Counter()
for item in ip_address:
    c[item] += 1
print(c)




