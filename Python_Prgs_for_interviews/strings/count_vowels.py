sentence = input("enter the string:")
string = sentence.lower()
count = 0
list1 = ["a", "e", "i", "o", "u"]
for char in string:
    if char in list1:
        count = count+1
print("number of vowels in the string is", count)

