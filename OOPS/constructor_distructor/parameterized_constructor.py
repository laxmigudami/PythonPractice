#This constructor accepts and stores arguments passed from the main() method during object creation. Below is an example code.
class Employee:
    def __init__(self, age, salary):
        self.age1 = age
        self.salary1 = salary


#main() method
John = Employee(22, 20000) #passing arguments to the parameterized constructor
print(John.age1)
print(John.salary1)