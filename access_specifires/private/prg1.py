class Employee:
    def __init__(self,name, sal):
        self.__name=name
        self.__sal=sal
    def __display(self):
        print("The name is", self.__name)
        print("The salary is",self.__sal)
obj1=Employee("Laxmi", 60000)
print(obj1.__name)

#NOTE
# double underscore __ prefixed to a variable makes it private.
# It gives a strong suggestion not to touch it from outside the class.
# Any attempt to do so will result in an AttributeError:'Employee' object has no attribute '__name'

#Name mangling -> we can access and modify the private variables