import re
path=r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileobj=open(path,"r")
string=fileobj.read()
pattern=r"b"
def finditerFunc():
    patternObj=re.compile(pattern)
    print("pattern obj is",patternObj)
    result=patternObj.finditer(string)
    print(result)
    for i in result:
        print(i)
finditerFunc()