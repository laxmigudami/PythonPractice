def is_title(s):
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            if 'a' <= s[i] <= 'z':
                return False
            elif 'A' <= s[i] <= 'Z':
                return True

print(is_title("hi How Are You"))