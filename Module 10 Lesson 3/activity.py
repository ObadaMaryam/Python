def sum(n):
    return n*(n+1)/2

#Sc0(1),As0(1)
def arraysum(a):
    sum=0
    for i in a:
        sum = sum+1

    return(sum)

a = [15, 20, 25, 30]
arraysum(a)
#The space Complexicity is n