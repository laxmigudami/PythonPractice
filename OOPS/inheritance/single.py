# In single inheritance, a child class inherits all the properties of a parent class.

class Car:
    length = '470cm'

    def drive(self):
        print("i can drive at a speed of 60km/hr")


class RaceCar(Car):

    def rashdrive(self):
        print("i can drive at a speed of 40km/hr")


maruti = RaceCar()
maruti.drive()
maruti.rashdrive()
