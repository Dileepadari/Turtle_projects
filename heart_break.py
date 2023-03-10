import turtle
import time
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Pen()
pen.color("red")
pen.fillcolor("red")
pen.begin_fill()
pen.left(45)
pen.forward(113)
i = 0
while(i<20):
    pen.left(9)
    pen.forward(9)
    i = i+1
pen.left(260)
i = 0
while(i<19):
    pen.left(10)
    pen.forward(9)
    i = i+1
pen.forward(117)
pen.end_fill()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.left(140)
pen.forward(55)
pen.right(30)
pen.forward(55)
pen.left(50)
pen.forward(80)
pen.left(90)
pen.forward(15)

pen.left(90)
pen.forward(70)
pen.right(50)
pen.forward(55)
pen.left(32)
pen.forward(80)
pen.end_fill()

time.sleep(2)