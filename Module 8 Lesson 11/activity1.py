class Cat:

    #Contructor
    def __init__(self, name,age):
        self.name = name
        self.age = age

    #Method
    def info(self):
        print("I am a cat. My name is "+ self.name+" and I am "+self.age+" days old")

    #method
    def make_sound(self):
        print("Meaow")

class Dog:

    #Contructor
    def __init__(self, name,age):
        self.name = name
        self.age = age

    #Method
    def info(self):
        print("I am a dog. My name is "+ self.name+" and I am "+self.age+" years old")

    #method
    def make_sound(self):
        print("Baow")


#Object creation
catobj = Cat("Mala" , "24")
dogobj = Dog("Rusty" , "1.5")

#iterating through objects
for pet in (catobj,dogobj):
    pet.info()
    pet.make_sound()
