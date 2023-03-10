import turtle
import time
screen = turtle.Screen()
screen.bgcolor("blue")
pen = turtle.Pen()
pen.color("black")
pen.speed(20)
i = 0
while(i<200):
    pen.forward(2*i)
    pen.left(i)
    i = i+1
time.sleep(2)
