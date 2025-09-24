def find_lcm(num1, num2):
    # Determine the larger number
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1
    return lcm


# Example usage with the numbers from the image (corrected input)
# The image shows "Enter Largest number : 20" and "Enter Smallest number: 80"
# This implies the user intended to find LCM of 20 and 80.
number1 = 20
number2 = 80

result_lcm = find_lcm(number1, number2)
print(f"The LCM of {number1} and {number2} is: {result_lcm}")