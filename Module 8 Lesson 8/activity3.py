class Parrot:

    #instance attributes
    def __init__(self, name,age):
         self.name = name
         self.age = age

    #inttance method
    def sing(self, song):
         return "{} sings {}".format(self.name, song)
    
    #method
    def dance(self):
         return "{} is dancing".format(self.name)

obj = Parrot("Blu", 5)

print("{} is {} years old".format(obj.name,obj.age))

print(obj.sing("Happy"))
print(obj.dance())