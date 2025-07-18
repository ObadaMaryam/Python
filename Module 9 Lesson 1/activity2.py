#open file in read mode
file_read = open(r"C:\Users\Azan Ar Computers\Desktop\Python\Module 9 Lesson 1\Recipe.txt", "r")
print("File in read mode -")
print(file_read.read())
file_read.close()

#open file in write mode
file_write = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 1\\Recipe.txt", "w")
#write in the file
file_write.write("File in write mode")
file_write.write("Hi! Its Mrya`s recipe")
file_write.close()

#open file in append mode
file_append = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 1\\Recipe.txt", "a")
#append file
file_append.write("file in append mode")
file_append.write("I hope you liked it")
file_append.close()