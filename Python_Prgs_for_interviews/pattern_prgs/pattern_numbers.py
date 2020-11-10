n = int(input("enter the number of rows:"))
for row in range(n):
    val = row+1
    dec = n-1
    for col in range(row+1):
        print(val , end=" ")
        val = val + dec
        dec = dec - 1

    print()