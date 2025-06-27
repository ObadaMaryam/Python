import turtle

# creating canvas
turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(500,400)

turtle.title("Wellcom to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for a in range(4):
    board.forward(200)
    board.left(90)
    a = a+1