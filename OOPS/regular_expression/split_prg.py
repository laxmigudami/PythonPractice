import re
path=r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj=open(path,"r")
string=fileObj.read()
pattern=r"hello"
def splitFunc():
    patternObj=re.compile(pattern)
    result=patternObj.split(string,2)
    print(result)
splitFunc()