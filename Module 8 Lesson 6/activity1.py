drink_list=["coca_cola", "sprite", "mint_margrita", "red_bull", "milk_shake", "mango_juice", "soda"]

#length
print("The lenght of the list is", len(drink_list))

#append
drink_list.append("apple_juice")
print("Updated list:", drink_list)

#Acceessing the elements of the list
print("Second element:", drink_list[1])
print("Fifth element:", drink_list[4])

#remove
drink_list.remove("red_bull")
print("Updated list", drink_list)

#sorting
drink_list.sort()
print("Sorted list:", drink_list)

#pop
drink_list.pop(3)
print("List after popping a drink out", drink_list)

#reverse
drink_list.reverse()
print("Reversed list:", drink_list)

#slicing
drink_list = drink_list[0:5]
print("List after slicing", drink_list)
