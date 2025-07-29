with open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 3\\advofveg.txt" , "w") as f:
    f.write("Adventages of Vegetables")

with open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 3\\advofveg.txt" , "r") as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)

f.close()