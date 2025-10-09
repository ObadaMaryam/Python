n = int(input("Enter a Number: "))

binary = bin(n)[2:]

longest_ones = max(binary.split("0"))
print("Longest consecutive 1's length:", len(longest_ones))