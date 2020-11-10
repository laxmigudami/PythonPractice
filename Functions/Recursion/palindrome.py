# string palindrome using recursion
def palindrome(a):
    if len(a) < 1:
        return
    else:
        if a[0] == a[-1]:
            return palindrome(a[1:-1])

        else:
            return False


# main() function
a = str(input("enter a string:"))
if palindrome(a):
    print("string is a palindrome")
else:
    print("string is not a palindrome")
