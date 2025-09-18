def numofbits(n):
    ones = 0
    zeros = 0

    while (n):
        #use AND Operator
        if(n&1 == 1):
            ones = ones+1
        else:
            zeros = zeros+1
        n = n >> 1
    print("Ones=",ones)
    print("Zeros=",zeros)

n = int(input("Enter the Number: "))
numofbits(n)