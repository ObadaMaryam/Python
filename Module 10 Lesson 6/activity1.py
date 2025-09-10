from math import sqrt

number = int(input("Enter the Number: "))

if number > 1:
    for a in range(2, int(sqrt(number)+1)):
        if number%a == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

else:
    print("Not a Prime Number")