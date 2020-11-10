# Write a program to search for a character in a given string and return the corresponding index.

def search_character(string, key):
    for index, c, in enumerate(string):
        if c == key:
            print(f'Character {c} is at index {index }')



search_character('hello world', 'w')
search_character('hello world', 'd')
  