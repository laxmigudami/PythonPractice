def word_count(s):
    count = 0
    for i in s:
        print(i)
        if i == " ":
            count += 1

    return count + 1


print(word_count("i am going to pass this exam"))
