import re
path=r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj=open(path,"r")
string=fileObj.read()
pattern=r"hello"
def fullmatchFunc():
    patternObj=re.compile(pattern)
    result=patternObj.fullmatch(string)
    print(result)
fullmatchFunc()