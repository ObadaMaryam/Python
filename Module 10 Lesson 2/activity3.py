def OnSquareTime(n):
    i = 0 
    for i in range (0, n):
        for j in range(0, n):
            print("*", end=" ")
            i = i+1
        print(" ")
    print("When n is ", n, "Iterations =", i)

OnSquareTime(5)
OnSquareTime(15)
OnSquareTime(30)