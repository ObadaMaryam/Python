rows = int(input("Enter the number of rows: "))

for b in range(1,rows+1):
    for a in range(b):
        print("*", end=" ")
    print()