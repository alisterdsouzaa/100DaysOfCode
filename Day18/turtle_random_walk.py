# Make a square with turtle

from turtle import Turtle, Screen
import random

eve = Turtle()
eve.shape("turtle")
eve.speed("fast")

colours = ["red", "green", "cyan", "royal blue", "yellow", "pink", "gold", "DarkOrchid", "silver"]

# Direction values in angles
direction = [0,
             90,
             180,
             270
             ]

# def random_walk():
#     eve.pensize(1)
#     eve.pendown()
#     direction = random.randint(1, 5)
#     distance = random.randint(10, 100)
#     if direction == 1:
#         eve.forward(distance)
#     elif direction == 2:
#         eve.backward(distance)
#     elif direction == 3:
#         eve.right(distance)
#     elif direction == 4:
#         eve.left(distance)
#     else:
#         eve.right(distance)


for _ in range(100):
    eve.color(random.choice(colours))
    eve.forward(30)
    eve.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
