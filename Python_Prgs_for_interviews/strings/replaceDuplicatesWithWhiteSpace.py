def replace_duplicate(string):
    temp = ""
    for i in string:
        if i not in temp:
            temp += i
        else:
            temp += " "
    return temp


print(replace_duplicate("hello"))
