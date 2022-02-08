import turtle

a= turtle.Turtle()
turtle.Screen().bgcolor("yellow")
body="red"
glasses="cyan"

a.speed(10)
a.pensize(15)
a.fillcolor(body)
a.begin_fill()

a.right(90)
a.forward(60)
a.right(180)
a.circle(30,-180)
a.right(180)
a.forward(200)

a.right(180)
a.circle(100,-180)

a.backward(20)
a.left(15)
a.circle(500,-20)
a.backward(20)

a.circle(30,-180)
a.left(7)
a.backward(70)

a.up()
# a.left(90)
a.left(90)
a.forward(10)
a.right(90)
a.down()
a.right(240)
a.circle(95,-70)
a.end_fill()
80
def glass():
    a.up()
    a.right(240)
    a.forward(120)
    a.left(90)
    a.forward(5)
    a.right(90)
    a.down()

    a.fillcolor(glasses)
    a.begin_fill()
    a.right(150)
    a.circle(80,-60)
    a.left(130)
    a.forward(140)
    a.left(110)
    a.circle(87,-60)
    a.right(50)
    a.backward(138)
    a.end_fill()

def bag():

   a.up()
   a.back(80)
   a.right(90)
   a.forward(10)
   a.left(90)
   a.forward(10)
   a.down()

   a.fillcolor(body)
   a.begin_fill()
   a.left(180)
   a.forward(18)
   a.circle(30,90)
   a.forward(87)
   a.left(90)
   a.forward(40)
   a.end_fill()

glass()
bag()

turtle.done()