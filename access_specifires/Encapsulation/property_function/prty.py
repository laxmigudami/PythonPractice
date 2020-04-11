class Girl:
    def __init__(self,name):
        self.__name=name
    def getmethod(self):
        print("getmethod is called")
        print(self.__name)
    def setmethod(self,New):
        print("setmethod is called")
        self.__name=New
    object=property(getmethod, setmethod)
a1=Girl("laxmi")
a1.object
a1.object="asha"
a1.object


