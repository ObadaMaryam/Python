str = input("Enter a string: ")

print("All substrings are: ")

for m in range(len(str)):
    for n in range(m + 1, len(str)+1):
        print(str[m : n])