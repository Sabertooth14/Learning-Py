import turtle

x= turtle.Turtle()
x.color("blue","cyan")
x.speed(8)
x.begin_fill()
for i in range(35):
    x.forward(200)
    x.left(175)
    x.forward(200)
    # x.left()
x.end_fill()

turtle.done()