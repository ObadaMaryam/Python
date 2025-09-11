from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)+1)):
        (num)
        if num % i == 0:
            return False
    return True

print("Two-digit prime numbers are: ")

for number in range(10, 100):
    if is_prime(number):
        print(number, end="")