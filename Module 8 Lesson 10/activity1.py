class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
            print("Your name is ", self.name)
            print("The id number is given in", self.idnumber)

class employee(Person):

    def __init__(self,salary,position,name,idnumber):
        self.salary = salary
        self.postion = position

        super().__init__(name,idnumber)

    def displayforemployee(self):
        print("Your salary is ", self.salary)
        print("The Position is given in ", self.postion)

obj = employee("100,000","Director","Maryam","1019")

obj.displayforemployee()
obj.display()



