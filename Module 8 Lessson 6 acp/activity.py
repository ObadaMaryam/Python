import random

number = random.randint(1 , 10)
solved = False

print("Guess the number:")

while not solved:
    guess = int(input())

    if guess > number:
        print("To High")
    elif guess < number:
        print("To Low")
else:
        print("Correct")
        solved = True