class Parrot:

    def __init__(self, name,age):
         self.name = name
         self.age = age

obj = Parrot("Blu", 5)

print("{} is {} years old".format(obj.name,obj.age))