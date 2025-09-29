def oddOcc(array):
    result = 0 
    for elememt in array:
        result = result ^ elememt

    return result

array = []
n = int(input("Enter the size of array: "))

while(n):
    element = int(input("Enter the element: "))
    array.append(element)
    n = n - 1

print("The odd occuring number: ", oddOcc(array))
