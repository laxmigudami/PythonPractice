# An abstract class having a normal method and an abstract method

from abc import ABC


class Shape(ABC):
    def print(self):
        print("i am a normal method defined inside the abstract class Shape")

    def calculate_area(self):  # abstract method
        pass


class Rectangle(Shape):
    length = 5
    breadth = 3

    def calculate_area(self):
        return self.length * self.breadth


class Circle(Shape):
    radius = 4

    def calculate_area(self):
        return 3.14 * self.radius


rec = Rectangle()
cir = Circle()
print("area of rectangle:", rec.calculate_area())
print("area of circle:", cir.calculate_area())

# the normal method is called from the main() method
# using an object created for the child class 'Rectangle'
