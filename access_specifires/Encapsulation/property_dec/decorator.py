 #@property decorator allows us to define properties easily without calling the property() function manually.
#@property decorator is aYU built-in decorator in Python for the property() function.

class Person:
    def __init__(self):
        self.__name=''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @name.deleter
    def name(self):
        del self.__name

p1=Person()
print(p1.name)
p1.name="laxmi"
print(p1.name)

#The above person class includes two methods with the same name name(), but with a different number of parameters.
# This is called method overloading.
# The name(self) function is marked with the @property decorator which indicates that the name(self) method is a getter method
# and the name of the property is the method name only, in this case name.
# Now, name(self, value) is assigning a value to the private attribute __name.
# So, to mark this method as a setter method for the name property, the @name.setter decorator is applied.
# This is how we can define a property and its getter and setter methods.

