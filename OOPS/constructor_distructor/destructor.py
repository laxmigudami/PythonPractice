
# Destructors are also special methods that are used to perform final operations like closing files,
# closing database connections, cleaning up the buffer or cache, etc. This method gets invoked for the following two reasons.

# When we explicitly delete an object created for a class using the keyword 'del'
# When an exception occurs in the __init__ method while initializing an object
class Employee:
    def __init__(self, age, salary):
        self.age1 = age
        self.salary1 = salary
    def __del__(self):  #destructor
        print("Destructor called and the class 'Employee' deleted")

#main() method
John = Employee(22, 20000)
print(John.age1)
print(John.salary1)
del John #deleting the object 'John' and calling the destructor