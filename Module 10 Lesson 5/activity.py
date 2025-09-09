number = int(input("Enter the Number: "))
print("The number you endered is ", number)

number_str = str(number)
reverse_str = number_str[::-1]
reverse_number = int(reverse_str)
print("The reverse number is ", reverse_number)

if number == reverse_number:
    print("Palindrome")
else:
    print("Not a Palindrome")