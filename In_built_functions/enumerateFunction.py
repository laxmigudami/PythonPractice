# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

# enumerate(iterable, start=0)
#
# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is
#               to be started, by default it is 0


tasks = [ "eat", "sleep", "repeat"]
for i in enumerate(tasks):
    print(i)

for count_, item in enumerate(tasks, 100):
    print(count_, item)

