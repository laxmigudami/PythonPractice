#sequence of characters and a character is a symbol be it an alphabet, special etc
# similarly how integers are converted to binary values by the compiler
# characters are converted to unicode values in the python

string1= " i am a intelligent girl"
print(string1[3])
# print(string1[25])  #------>leads to index error out of range error
print(len(string1))

# immutable type
# del string1

# escape sequence ---> this indicates  the compiler that the character followed by should be simply ingnored
string2 = 'I\'m in love with the python language'
print(string2)

# also we can tell the compiler to ignore the escape sequence by placing a r or R before your string.
# a raw string can ignore escape sequence
# useful when string contains a backslash
string3 = R'i would prefer learning python\java\both'
print(string3)

a = 5
# single formatting
b = "My name XYZ and my age is just {}"
print(b.format(a))

# multiple formatting
c = "My name is XYZ and my age is just {}. Also i have a sibling who's age is also {}"
print(c.format(a, a))




