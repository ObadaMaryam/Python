my_tuple = ("Maryam", "Mahnoor", "Alina", "Sara")

#accessing an element
print(my_tuple[3])

#slicing
print(my_tuple[0:4])

#nested tuple
new_tuple = ("Mrya",  ("Maryam", "Mahnoor", "Alina", "Sara"))
print(new_tuple)

#iteration
for letter in new_tuple:
    print("Hi!", letter)