file1 = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2\\advofmilk.txt", "r")
file2 = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2\\updated.txt", "w")
for line in file1.readlines():
    if not(line.startswith("Milk")):
        print(line)
        file2.write(line)

file2.close()
file1.close()