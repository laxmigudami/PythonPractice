# Dictionary Comprehension
# Building a dict of word and length pair

words = "This is a bunch of words"
d = {word: len(word) for word in words.split()}
# print(d)

# flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.items())
f = {value: key for key, value in d.items()}
# print(f)

# The items() method returns a view object.
# The view object contains the key-value pairs of the dictionary, as tuples in a list.

# searching for a word in the file

s = {word.strip() for word in open("words.txt")}
# print(s)
sentence = "Hello there. this is bunch of words aaronical and resnub"
w = {word: word in s for word in sentence.split()}
# print(w)


sentence = '''Python is is is is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language 
for scripting and rapid application development in many areas on most platforms.'''

dict_word_count = {
    word: sentence.count(word) for word in sentence.split(' ')
}
# print(dict_word_count)

# counting the number of each character in the string
my_string = 'guido van rossum'
dict_char_count = {c: my_string.count(c) for c in my_string}
# print(dict_char_count)

# dinctionary of character and ascii value pairs
s = 'abcABC'
dict_ascii = {c: ord(c) for c in s}
# print(dict_ascii)

# tallest building
tall_buildings = {
    'burj khalifa': 828,
    'Shanghai_Tower': 632,
    'Abraj_Al_Bait_Clock Tower': 601,
    'Ping_An_Finance_Centre_Shenzhen': 599,
    'Lotte World Tower': 554.5,
    'World Trade Center': 541.3
}


def to_feets(m):
    return round(m * 3.28)


tall_buildings_feets = {building: to_feets(height) for building, height in tall_buildings.items()}
# print(tall_buildings_feets)
# creating dictionary of city and population pairs using dict comprehension

cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]

population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]
# city_pop = {city: p for city in cities for p in population}
city_pop = {city: population for city, population in zip(cities, population)}
# print(city_pop)

# Building a dictionary with type and data mapping
data = [1, 1.2, 'hello', len, True, (1, 2, 3), {9, 8, 6}, ['apple', 'ibm', 'yahoo']]
type_data = { type(item):data for item in data}
print(type_data)

# Counts the occurance of each word in the text file and prints the most and least repeated words
with open('read.txt', 'r') as f:
    text = f.read()
    d = {
        word: text.count(word)
        for word in text.split(' ')
    }






