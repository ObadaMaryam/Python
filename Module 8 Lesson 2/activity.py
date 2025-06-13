height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height * height

print("Your bmi is" , bmi)

if (bmi < 18.5):
    print("You are underweight")

elif (bmi <= 24.9):
    print("You are healthy")

elif (bmi <= 29.9):
    print("You are overweight")

else:
    print("Your are extremely obese")
