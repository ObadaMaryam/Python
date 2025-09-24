def cir_output(X, Y, Z):
    A = (X & Y) | (Y & Z)
    return A

print("X Y Z | A")
for X in [0,1]:
    for Y in [0,1]:
        for Z in [0,1]:
            print(X, Y, Z, "|" , int(cir_output(X,Y,Z)))