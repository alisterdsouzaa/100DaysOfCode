# Make a square with turtle

from turtle import Turtle, Screen
import random

eve = Turtle()
eve.shape("circle")

colours = ["red", "green", "cyan", "royal blue", "yellow","pink","gold","white","DarkOrchid","silver" ]


def draw_shape(number_of_side):
    """Draws the shape provided by the i/p num of sides"""
    for _ in range(number_of_side):
        angles = 360 / number_of_side
        eve.forward(100)
        eve.right(angles)


for shape_side in range(3, 11):
    eve.color(random.choice(colours))
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()
