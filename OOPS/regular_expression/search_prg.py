import re

path = r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj = open(path, "r")
string = fileObj.read()
pattern = r"hello"


def searchFunc():
    patternObj = re.compile(pattern)
    result = patternObj.search(string, 2, 66),
    print(result)


searchFunc()
