import turtle

# creating canvas
turtle.Screen().bgcolor("Green")

sc = turtle.Screen()
sc.setup(500,400)

turtle.title("Wellcom to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# first triangle for star
board.forward(200) # draw base

board.left(120)
board.forward(200)

board.left(120)
board.forward(200)

board.penup()
board.right(150)
board.forward(100)

# second teiangle for star
board.pendown()
board.right(90)
board.forward(200)

board.right(120)
board.forward(200)

board.right(120)
board.forward(200)

turtle.done()