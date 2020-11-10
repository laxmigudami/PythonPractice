# factorial of the number say n will be the product of all positive numbers less than or equal to n
# 5!= 5*4*3*2*1





# 5! = 5*4*3*2*1

def fact(num):
    if num == 0 or num == 1:

        return 1
    else:
        return num *fact(num-1)
print(fact(5))