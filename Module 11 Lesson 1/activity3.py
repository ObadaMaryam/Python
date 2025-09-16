def numberofbits (n):
    count = 0

    while(n>0):
        count = count + 1
        n = n >> 1
    return count

n = 16
print("Total Bits: " , numberofbits(n))