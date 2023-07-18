# Make a square with turtle

from turtle import Turtle, Screen

eve = Turtle()
eve.shape("turtle")
eve.color("green")
eve.pencolor("red")

for _ in range(10):
    eve.pendown()
    eve.forward(10)
    eve.penup()
    eve.forward(10)


screen = Screen()
screen.exitonclick()
