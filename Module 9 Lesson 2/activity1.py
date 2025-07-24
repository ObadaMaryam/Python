# open the file and read its content
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2\\advofmilk.txt","r")
print(file.read())
file.close()

#open file and read its 36 characters
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2\\advofmilk.txt","r")
print(file.read(36))
file.close()

#append file
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2\\advofmilk.txt","a")
file.write("This Adventages is write by Maryam.")
file.close()