def func(a):
    if a==0:
        return
    else:
        print(a)
        func(a-1)
# main() function
func(3)