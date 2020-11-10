# In this type of inheritance, more than one child classes inherit all the properties of the same parent class.
#parent class
class Car:
  length = '470cm'
  def drive(self):
        print("I can drive at a speed of 60km/hr")

#child class 1
class RaceCar1(Car):
    def rashdrive1(self):
        print("I can drive at a speed of 40km/hr")

#child class 2
class RaceCar2(Car):
    def rashdrive2(self):
        print("I can drive at a speed of 30km/hr")

#main() method
maruti = RaceCar2()
maruti.drive()
maruti.rashdrive2()