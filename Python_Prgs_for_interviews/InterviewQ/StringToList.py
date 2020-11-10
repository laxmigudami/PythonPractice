# How to convert a string to a list and vice-versa
def convert_to_string(anylist):
    return ' '.join(anylist)

def convert_to_list(anystring):
    return anystring.split()

print(convert_to_list("laxmi Gudami"))
print(convert_to_string(["laxmi", "gudami", "tester", "test yantra"]))
