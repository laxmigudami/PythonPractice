# wap to to get the bellow output
sentence = "python is a programming language"
# d = {'p':['python', 'programming'] , 'i': ['is'] , 'a': ['a'] , 'l' : ['language'] }

from collections import defaultdict
d = defaultdict(list)
words = sentence.split()
for word in words:
    d[word[0]].append(word)
print(d)