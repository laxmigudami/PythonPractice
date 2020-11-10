def sum(num):
    if(num != 0):
        return num + sum(num-1)
    else:
        return  0
    # main() function
res = sum(3)
print(res)
