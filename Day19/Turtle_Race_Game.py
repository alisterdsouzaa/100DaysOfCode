import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your turtle choice", prompt="Which turtle will win the race? "
                                                                       "Enter your colour from this list = ['red', "
                                                                       "'orange', 'yellow', 'green', 'blue',"
                                                                       "'purple']: ")
print(user_choice)
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-60, -30, 0, 30, 60, 90]
all_turtles = []

for turtle_index in range(0, 6):
    eve = Turtle(shape="turtle")
    eve.color(colors[turtle_index])
    eve.penup()
    eve.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(eve)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_choice:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You loose. The winning turtle is {winning_turtle}")
                is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
