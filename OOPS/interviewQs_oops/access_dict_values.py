# Write a Custom class which can access the values of dictionaries using d['a'] and d.a


class MyDict:
    def __init__(self, d):
        self._dict = d

    def __getitem__(self, item):
        return self._dict[item]

    def __

