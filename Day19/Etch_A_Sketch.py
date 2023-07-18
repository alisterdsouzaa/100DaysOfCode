# Etch a Sketch project using turtle.
# Just run and make your sketch using w,a,s,d key from the keyboard.
from turtle import Turtle, Screen

eve = Turtle()
screen = Screen()
screen.bgcolor()
eve.color("brown")
eve.pendown()


def forward():
    eve.forward(10)


def backward():
    eve.backward(10)


def right():
    eve.right(10)


def left():
    eve.left(10)


def clear():
    eve.clear()
    eve.penup()
    eve.setposition(0, 0)
    eve.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="a", fun=left)
screen.onkey(key="c", fun=clear)
screen.onkeypress(key='w', fun=forward)

screen.exitonclick()
