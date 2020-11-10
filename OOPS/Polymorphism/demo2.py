# polymorphism with inheritance

class Car:
    def drive(self):
        print("i am driving with the speed of 40km/hr")

class RaceCar:
    def drive(self):
        print("i am driving with the speed of 120km/hr")


obj1 = Car()
obj2 = RaceCar()
print(obj1.drive())
print(obj2.drive())