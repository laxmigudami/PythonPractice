class Car:
    length = '470cm'

    def drive(self):
        print("I can drive at a speed of 60km/hr")


# child class
class RaceCar1(Car):
    def rashdrive1(self):
        print("I can drive at a speed of 40km/hr")


# grandchild class
class RaceCar2(RaceCar1):
    def rashdrive2(self):
        print("I can drive at a speed of 30km/hr")


# main() method
maruti = RaceCar2()
maruti.drive()
maruti.rashdrive1()
maruti.rashdrive2()
