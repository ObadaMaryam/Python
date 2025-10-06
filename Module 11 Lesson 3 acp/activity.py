n = int(input("Enter the number: "))

binary = bin(n)[2:]

reversed_binary = binary[::-1]

results = int(reversed_binary, 2)

print("Original Binary:", binary)
print("Reversed Binary:", reversed_binary)
print("New Number:", results)