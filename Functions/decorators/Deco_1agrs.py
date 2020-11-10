def dec_num(func):
    def inner(a):
        if a < 0:
            a = -a
            func(a)
    return inner
@dec_num
def num(a):
    print(a)
num(-10)




