# open the file and read its content
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
print(file.read())
file.close()

#open file and read its 21 characters
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
print(file.read(21))
file.close()

#read and print first line
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
print(file.readlines())
file.close()

#read and print multiple line
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#read and print all lines
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
print(file.readlines())
file.close()

#read by loops
file = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 2 acp\\disadvofmilk.txt","r")
for x in file:
    print(x)
file.close()