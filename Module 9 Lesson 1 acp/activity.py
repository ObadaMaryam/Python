#open file
file = open(r"C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 1 acp\\Sample_File.txt")

#read file
print(file.read())

#open file in write mode
file_write = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 1 acp\\Sample_File.txt", "w")
#write in the file
file_write.write("File in write mode")
file_write.write("Hi! This Doc is written by Obada_Maryam")
file_write.close()

#open file in append mode
file_append = open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 1 acp\\Sample_File.txt", "a")
#append file
file_append.write("file in append mode")
file_append.write("I wish you liked it")
file_append.close()