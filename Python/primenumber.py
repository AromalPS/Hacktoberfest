# Python Program to find Prime Number
 
Number = int(input(" Please Enter any Number: "))
count = 0

for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        count = count + 1
        break

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)