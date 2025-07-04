import turtle

#clcoding.com
m = turtle.Turtle()
m.speed(0)
v = turtle.Turtle()
v.speed(0)
turtle.bgcolor("black")
for i in range(150):
    m.color("red")
    m.circle(i)
    m.forward(60)
    m.right(60)
    v.circle(i)
    v.forward(60)
    v.color("blue")
    v.right(60)

turtle.done()

