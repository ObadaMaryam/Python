def divide(dividend, divisor):

    sign = (-1 if (dividend < 0 ) ^ (divisor < 0) else 1)

    dividend  = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if(temp + (divisor << i) <= dividend):
            temp = temp + divisor << i
            quotient = quotient | 1 << i


    if sign == -1:
        quotient = quotient - quotient
    return quotient
    
a = int(input("Enter A: "))
b = int(input("Enter B: "))
print(divide(a,b))