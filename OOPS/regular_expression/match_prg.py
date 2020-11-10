import re
path=r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\stringdata.txt"
fileObj=open(path,"r")
string=fileObj.read()
pattern=r"\w+@\w+\.\w{2,3}"
#pattern=r"gudamilaxmi444@gmail.com"
def matchFunc():
    patternObj=re.compile(pattern)
    result=patternObj.match(string)
    print(result)
matchFunc()