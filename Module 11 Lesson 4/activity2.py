def power4(num):
    count = 0

    if num & ~(num & (num-1)):
        while num>1:
            num = num >> 1
            count = count + 1

    if count % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter the Number: "))
if power4(num):
    print("The number is a power of 4")
else:
    print("The number is not a power of 4")
    