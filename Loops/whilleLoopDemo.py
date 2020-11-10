# prg to calculate the sum of all numbers less than a given number
number = 7
sum = 0
i = 0
while i < number:
    sum = sum + i
    i = i + 1
print(sum)

even_numbers = [2, 4, 6, 8, 10]
for i in even_numbers:
    print(even_numbers)
    print(i)

for i in range(2, 12, 2):  # (lower limit, upperlimit, difference between numbers)

    print(i)
#prg to print the pattern
for i in range(1, 5):
    for j in range(i):
        print(j+1, end=" ")
    print()
# 1 i=1 j=0
# 1 2 i=1 j=1+1
# 1 2 3
# 1 2 3 4
# control statements in the python
# 3 control statements
# break --->whenever a loop encounters a break statement it terminates the loop and the
# control shifts to the immediately next statement outside the loop
# continue--> whenever a loop encounters a continue statement, the control shifts to the beginning of the loop
