class Laptop:

    #Constructor
    def __init__(self):
        self.__maxprice = "850"

    #method
    def sell(self):
        print("Selling Price:"+ self.__maxprice)

    #method
    def setMaxPrice(self, price):
        self.__maxprice = price

#Object creation
obj = Laptop()

#update the maxprice
obj.__maxprice = "1,200"
obj.sell()

#updated maxprice
obj.setMaxPrice("1,200")
obj.sell()