#Leap year has 29 days in the month of feb. it occurs every four years.
# prg to check if its leap year or not
#2000, 2004, 2008....





year = int(input("enter year:"))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0:
    print("leap year")
elif year % 100 == 0:
    print("leap year")
else:
    print("not a leap year")