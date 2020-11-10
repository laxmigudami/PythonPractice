# polymorphism with user defined methods
class Rectangle:
    width = 6
    breadth = 5

    def calculate_area(self):
        return self.width * self.breadth


class Circle:
    radius = 5

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle()
cir = Circle()

print(rec.calculate_area())
print(cir.calculate_area())
