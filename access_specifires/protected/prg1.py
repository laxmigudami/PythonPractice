class Employee:
    def __init__(self, name, sal):
        self._name = name  # protected attribute
        self._sal = sal  # protected attribute

    def _display(self):
        print("Name is:", self._name)
        print("salary is:", self._sal)


obj1 = Employee("vivek", 20000)
obj1._display()
# print(obj1._name)
# print(obj1._sal)
obj1._name = "laxmi"
print(obj1.name)

# note
# Protected members of a class are accessible from within the class and are also available to its sub-classes.
# No other environment is permitted access to it.
# This enables specific resources of the parent class to be inherited by the child class.

# Python doesn't have any mechanism that effectively restricts access to any instance variable or method.
# Python prescribes a convention of prefixing the name of the variable/method with single or

# double underscore to emulate the behaviour of protected and private access specifiers.
