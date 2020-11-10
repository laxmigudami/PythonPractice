#it is a sequence or a phrase if we reversed it it will be the same as the original
# def palindrome(num):
#     l1 = num[::-1]
#     if l1 == num:
#         print("the given sequence is a palindrome")
#     else:
#         print("the given sequence is not a palindrome")
# palindrome("madam")
# palindrome("1212")


string = input("enter the string:")
revString = string[::-1]
if revString == string:
    print("palindrome")
else:
    print("not palindrome")
