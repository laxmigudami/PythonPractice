#The property() method in Python provides an interface to instance attributes.
# It encapsulates instance attributes and provides a property
# The property() method takes the get, set and delete methods as arguments and returns an object of the property class.
#prop=property(getter, setter, deleter, docstring)

class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() is called')
        self.__name=name
    def getname(self):
        print('getname() is called')
        return self.__name
    name=property(getname, setname)
p1=person()
p1.name="Steve"
print(p1.name)


# In the above example, property(getname, setname) returns the property object and assigns it to name.
# Thus, the name property hides the private instance attribute __name.
# The name property is accessed directly, but internally it will invoke the getname() or setname() method

# "@property decorator makes it easy to declare a property instead of calling the property() function"
