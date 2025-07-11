class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id

    #Destructor
    def __del__(self):
        print("Destuctor called. Employee deleted.")

#Object creation
obj = Employee("Maryam", "1909")

print("The employee id of " + obj.name+" is "+obj.id)

del obj