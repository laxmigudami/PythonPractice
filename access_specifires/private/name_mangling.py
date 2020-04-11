class Employee:
    def __init__(self,name, sal):
        self.__name=name
        self.__sal=sal
    def __display(self):
        print("The name is", self.__name)
        print("The salary is",self.__sal)
obj1=Employee("Laxmi", 60000)
#print(obj1.__name)
# object._class__variable
print(obj1._Employee__sal)
obj1._Employee__display()
obj1._Employee__sal=20000
print(obj1._Employee__sal)



#NOTE:
#Python performs name mangling of private variables.
# Every member with double underscore will be changed to _object._class__variable.
# If so required, it can still be accessed from outside the class, but the practice should be refrained.