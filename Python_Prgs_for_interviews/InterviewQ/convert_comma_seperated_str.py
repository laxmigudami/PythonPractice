# Covert the string "Hello welcome to Python" to a comma separated string.string = "Hello welcome to Python"
def convert_to(string):
    temp = string.split()
    print(','.join(temp))

convert_to("Hello welcome to Python")


