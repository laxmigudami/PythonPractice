import re
path=r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj=open(path,"r")
string=fileObj.read()
pattern=r"hello"
def subnFunc():
    patternObj=re.compile(pattern)
    result=patternObj.subn("hai",string,1)
    print(result)
    for i in result:
        print(i)
subnFunc()