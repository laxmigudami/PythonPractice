import re

path = r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj = open(path, "r")
string = fileObj.read()
pattern = r"python"


def findallFunc():
    patternObj = re.compile(pattern)
    result = patternObj.findall(string)
    for i in result:
        print(i) 


findallFunc()
