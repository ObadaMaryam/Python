m = int(input("Enter the number: "))
num=m
p=0
while m>0:
    q=m%10
    p=p+q*q*q
    m=m//10
if p==num:
    print(num,"is a Armstrong Number.")
else:
    print(num,"is not a Armstrong Number.")