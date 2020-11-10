def fact(num):
    f=1
    for i in range(1, num+1):
        f = f*i
    print("the factorial of", num, "is", f)
num = int(input("enter the number:"))
fact(num)
# keyward arguments are used to overcome the drowbacks that are there in the positional argumnets
def employee(name, age, sal):
    print("name of the employee is", name)
    print(" age of the employee is:", age)
    print("salary of the employee is :", sal)
employee(name ="laxmi", sal = 25000, age = 25)

