m = int(input("Enter the working days: "))
n = int(input("Enter the days of absent: "))

attendence = m-n
if (attendence < 75):
    print("You are eligible for exams")

else:
    print("You are not eligible for exams")