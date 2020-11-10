#whenever user creates an object default constructor gets invoked
# there are 2 types of constructors:
# 1. default c
# 2. Parameterized constructor

class Employee:
  age = 22  #class variable#default constructor used to initialize 'age' with the value 22def __init__(self):self.age = 22

#main() method
John = Employee() #creating object (John) for the class 'Employee'. Once the object is created, the Python interpreter calls the default constructor
print(John.age)
#printing the value stored in the variable 'age' using the object 'John'
print(Employee.age)