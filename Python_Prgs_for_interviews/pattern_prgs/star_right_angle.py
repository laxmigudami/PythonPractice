# n = int(input("enter the number of rows:"))
# for i in range(n + 1):
#     print(" " * (n - i) + "* " * i)
# #     print("  " * (n - i) + "* " * i)
# #     # print("* "*i)


n = int(input("enter the number of rows:"))
for i in range(n + 1):
    print("* " * i)
for i in range(n-1, 0, -1):
    print("* " * i)