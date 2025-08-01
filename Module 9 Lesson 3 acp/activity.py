with open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 3 acp\\disadvofveg.txt" , "w") as f:
    f.write("Disadventages of Vegetables")

with open("C:\\Users\\Azan Ar Computers\\Desktop\\Python\\Module 9 Lesson 3 acp\\disadvofveg.txt" , "r") as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)
f.close()

#create a file
#new_file = open("My new doc.txt", "x")
#new_file.close()

#check if a file exist
import os
if os.path.exists("My document.txt"):
    os.remove("My document.txt")
else:
    print("File does not exixt.")

#create a new if it doesn`t exist
new_file = open("My document.txt" , "x")
new_file.close()
new_file1 = open("My document.txt" , "w")
new_file1.write("Hello! This is Maryam`s File")
new_file1.close()

#Remove file
os.remove("My new doc.txt")