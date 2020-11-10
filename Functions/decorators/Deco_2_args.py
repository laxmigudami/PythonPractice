def deco_sub(func): #func stores the address of the decorated function
    def inner(a, b):
        if a < b:
            a, b = b, a
        func(a, b)

    return inner


@deco_sub
def sub(a, b):
    print(a - b)


sub(5, 10)
# execution
# as soon as control sees the def keyward it will create the block of memory in the method ara
#  and stores the address of that in deco_sub--->0x11
# here it wants to decorate the fun sub so it will create that function in method area
# and stores the address of that body in sub --->0x22
# and @deco_sub ---> sub=deco_sub(sub)
# it will goes to 0x11 with carrying 0x22 that stores 0x22 in func and creates inner and returns the inner address 0x33
# now sub is overrided with 0x33 and whenever we call function sub it goes to 0x33
# directly and executes from there it goes to ox22 and prints the result---------

