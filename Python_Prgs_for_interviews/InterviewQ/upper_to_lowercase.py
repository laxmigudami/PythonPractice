# Write program to convert upper case to lower case and vice-versa without using inbuilt method.

def convert(any_string):
    l=[]
    for c in any_string:
        temp = ord(c)
        if temp >= 97 and temp <= 122:
            l.append(chr(temp-32))

        if temp>=65  and temp <= 90:
            l.append(chr(temp+32))
    return ''.join(l)

print(convert("Hello World"))
