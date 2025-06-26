def fact(a):
    if a == 1 or a == 2:
        return a
    else:
        return a * fact(a-1) 
    
num = int(input("Enter a number: "))

if num < 0:
    print("SORRY! factorial doesnot exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is" , fact(num))