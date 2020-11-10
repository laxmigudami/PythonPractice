from re import *

res = search('\A[FA]', 'FACE Prep')
if res:
    print("Found")
else:
    print("Not Found")
