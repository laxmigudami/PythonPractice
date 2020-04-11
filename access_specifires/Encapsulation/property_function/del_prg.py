class Person:
    def __init__(self,name):
        self.__name=name
    def getname(self):
        print("getmethod is called")
        print(self.__name)
    def setname(self,new):
        print("setmethod is called")
        self.__name=new
    def delname(self):
        print("deletemethod is called")
        del self.__name
    name=property(getname, setname, delname)
p1=Person("lax")
p1.name="stella"
p1.name
