import math

#Base class
class Polygon:
    def area(self):
        pass  # Abstract Method

#Rectangle class
class Rectangle(Polygon):
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#Square class
class Square(Polygon):
    def _init_(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

#Triangle class
class Triangle(Polygon):
    def _init_(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

#Circle class
class Circle(Polygon):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

#Testing
#Create objects and display areas
rect = Rectangle(20, 10)
print("Area of Rectangle:", rect.area())

sq = Square(4)
print("Area of Square:", sq.area())

tri = Triangle(18, 9)
print("Area of Triangle:", tri.area())

cir = Circle(11)
print("Area of Circle:", round(cir.area(), 2))