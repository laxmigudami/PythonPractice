def read():
    fileobj=open(r"C:\Users\LENOVO\PycharmProjects\python practice\regular_expression\pythondata.txt","r")
    res=fileobj.readlines()
    writedata(res)
def writedata(res):
    fileobj1=open(r"C:\Users\LENOVO\PycharmProjects\python practice\regular_expression\pythondata1.txt","w")
    l=[]
    for i in res:
        if i not in l:
            l.append(i)
    fileobj1.writelines(l)
    fileobj1.close()
read()
