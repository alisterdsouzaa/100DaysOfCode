# Make a square with turtle

from turtle import Turtle, Screen

eve = Turtle()
eve.shape("circle")
eve.color("green")

for _ in range(4):
    eve.forward(100)
    eve.right(90)

screen = Screen()
screen.exitonclick()
