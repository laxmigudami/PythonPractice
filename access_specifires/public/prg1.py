class Employee:
    def __init__(self,name, sal):
        self.name=name
        self.sal=sal
    def display(self):
        print("the name is ", self.name)
        print("the salary is ", self.sal)

obj1=Employee("laxmi" ,1000)
# print(obj1.name)
# print(obj1.sal)
# obj1.sal=10000
# print(obj1.sal)
obj1.display()

# pubic members can be accessed from any part of the program.Public members (generally methods declared in a class) are
# accessible/modifiable from outside the class.
# he object of the same class is required to invoke a public method