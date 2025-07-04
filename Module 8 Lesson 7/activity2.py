my_set = {1,2,3,3,3,4,4,4,4,5,5,5,6,6,7,8,}
print(my_set)

#add
my_set.add(10)
print(my_set)

set1 = my_set #(1,2,3,4,5,6,7,8,10)
set2 = {11,13,15,17,19}

#intersection
set_intersection = set1.intersection(set2)
print(set_intersection)

#union
set_union = set1.union(set2)
print(set_union)

#set difference
set_difference = set1.intersection(set2)
print(set_difference)

#set symmetric difference
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)