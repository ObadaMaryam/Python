import turtle
m = turtle.Turtle()
n = turtle.Screen()
colors = ["purple", "yellow", "green", "red", "orange"]
n.bgcolor("black")
m.speed("fastest")
m.hideturtle()
while True:
    for a in range(200):
        m.pencolor(colors[a%len(colors)])
        m.width(a/100 + 1)
        m.forward(a)
        m.left(59)
    m.right(239)
    for a in range(200, 0, -1):
        m.pencolor("black")
        m.width(a/100 + 7)
        m.forward(a)
        m.right(59)

        turtle.done()
