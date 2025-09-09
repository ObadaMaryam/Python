number = int(input("Enter a Number: "))

number_of_digits = len(str(number))
result = 0
temp = number

while temp > 0:
    digit = temp % 10 #finding rem
    result = result + digit ** number_of_digits
    temp = temp // 10 #finding div result

if number == result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
