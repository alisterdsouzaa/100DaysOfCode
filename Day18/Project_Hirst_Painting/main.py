# from colorgram import colorgram
# rgb_colours = []
# colours = colorgram.extract('Hirst_Painting.jpeg', 10)
#
# for colour in colours:
# """Extract colours form the img
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
screen = Screen()
screen.bgcolor("black")

colour_list = [(248, 247, 246), (234, 241, 247), (247, 240, 245), (244, 249, 246), (141, 163, 182), (14, 119, 185),
               (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97)]

kacey = Turtle()
kacey.speed(0)
kacey.color("white")
kacey.penup()
kacey.setheading(225)
kacey.forward(250)
kacey.setheading(0)
kacey.ht()
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    colour = random.choice(colour_list)
    kacey.begin_fill()
    kacey.pencolor()
    kacey.circle(5)
    kacey.dot(20, colour)
    kacey.end_fill()
    kacey.forward(50)

    if dot_count % 10 == 0:
        kacey.setheading(90)
        kacey.forward(50)
        kacey.setheading(180)
        kacey.forward(500)
        kacey.setheading(0)

screen.exitonclick()
