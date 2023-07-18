import random
import turtle
from turtle import *

colours = ["red", "green", "cyan", "royal blue", "yellow", "pink", "gold", "DarkOrchid", "silver"]

kacey = Turtle()
kacey.shape("turtle")
kacey.speed(0)

screen = Screen()
screen.bgcolor("black")

# Because Kacey is white
kacey.color("white")


def random_colour():
    """ This fun will return a random colour created by the shades of RGB"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_colours = (red, green, blue)
    return random_colours


for _ in range(0, 361):
    kacey.circle(100)
    kacey.color(random.choice(colours))
    kacey.setheading(kacey.heading() + 10)

screen.exitonclick()
