#create a file
#new_file = open("New doc.txt", "x")
#new_file.close()

#check if a file exist
import os
if os.path.exists("Document.txt"):
    os.remove("Document.txt")
else:
    print("File does not exixt.")

#create a new if it doesn`t exist
new_file = open("Document.txt" , "x")
new_file.close()
new_file1 = open("Document.txt" , "w")
new_file1.write("Hi! Its Mrya`s File")
new_file1.close()

#Remove file
os.remove("New doc.txt")


