from abc import ABC


class Shape(ABC):
    def cal_area(self):
        pass

    def print_statement(self):
        print("i am normal method")


class Rectangle(Shape):
    length = 10
    width = 20

    def cal_area(self):
        return self.width * self.length


class Circle(Shape):

    radius = 10

    def cal_area(self):
        return 3.14 * self.radius * self.radius



rec = Rectangle()
cir = Circle()
print(cir.cal_area())
print(rec.cal_area())
print(rec.print_statement())