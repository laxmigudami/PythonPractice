class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):
        self.__name=name
    def getname(self):
        return self.__name
p1=person()
print(p1.getname())

p1.setname("enemy")
print(p1.getname())
# NOTE:
#  p1.getname() method returns the value of attribute __name and
#  the setname() method assigns a value to it