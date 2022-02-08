import turtle
import math

p = turtle.Turtle()

#practice 
# p.fd(55)
# p.left(60)
# p.fd(55)
# p.left(30)
# p.fd(55)

#Create a square
# p.fd(100)
# p.left(90)
# p.fd(100)
# p.left(90)
# p.fd(100)
# p.left(90)
# p.fd(100)
p.color("red" )
# p.begin_fill()
# for i in range(4):
#     p.fd(100)
#     p.left(90)
# p.end_fill()

# p.penup()
# p.right(90)
# p.fd(50)
# p.pendown()

# p.color("red","yellow" )

# p.begin_fill()
# for i in range(4):
#     p.fd(100)
#     p.left(90)
# p.end_fill()
p.speed(9)
for i in range (1000):
    p.forward(math.sqrt(i))
    p.left(i%120)


turtle.done()