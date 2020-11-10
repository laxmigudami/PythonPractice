class Simple:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return iter(self._items)


s = Simple([1, 2, 3, 4, 5])
for item in s:
    print(item)
