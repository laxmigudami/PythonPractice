from abc import ABC


class Shape(ABC):  # abstract class

    def calculate_area(self):
        pass


class Rectangle(Shape):
    length = 5
    breadth = 3

    def calculate_area(self):
        return self.length * self.breadth


class Circle(Shape):
    radius = 4

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle()
cir = Circle()
print("area of a rectangle:", rec.calculate_area())
print("area of a circle:", cir.calculate_area())


# note
# abstract class will have abstract methods and abstract methods
# will not have any implementation
# implementation will be done in method of its sub classes
# If the implementation of the abstract method is not defined in the derived classes,
# then the Python interpreter throws an error.
# An abstract class can have both a normal method and an abstract method
# An abstract class cannot be instantiated, ie.,
# we cannot create objects for the abstract class
