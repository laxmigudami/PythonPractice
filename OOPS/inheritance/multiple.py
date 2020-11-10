# In Multiple inheritance, a child class inherits the properties of more than one parent class.
# We need to mention the names of the parent class as comma-separated in the child class.In the below example,
# the child class RaceCar inherits all the properties of Car1 and Car2.

class Car1:
    length = '470cm'

    def drive1(self):
        print("i can drive at a speed of 60km/hr")


class Car2:
    length = '400cm'

    def drive2(self):
        print("i can drive at a speed of 70km/hr")


class RaceCar(Car1, Car2):
    def rashdrive(self):
        print("i can drive at a speed of 40km/hr")


maruti = RaceCar()
maruti.drive1()
maruti.drive2()
maruti.rashdrive()