# PYTHON program to compare two radii
class Circle:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return 'Radius(r2) is greater'
        else:
            return "Radius (r1) is greater "

    def __eq__(self, other):
        if self.a == other.a:
            return "Radius are equal"
        else:
            return "Not equal"


r1 = Circle(12)
r2 = Circle(9)
print(r1 < r2)
r3 = Circle(6)
r4 = Circle(4)
print(r3 == r4)
