#wap to swap the two numbers without using 3rd variable

def swap(a,b):
    a,b = b,a
    return a, b
print(swap(5,6))