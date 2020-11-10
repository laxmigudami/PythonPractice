# Write a program to check if the given string is Palindrome or not without using reversed method.

def check_palindrome(string):
    if string == string[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


check_palindrome("malayalam")
