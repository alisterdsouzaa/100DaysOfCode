# Turtle Graphics Library. And using Pretty Table Package
'''
from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("Red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

'''

from prettytable import *
table = PrettyTable()
names = ["Pikachu", "Raichu", "Charmane"]
table.add_column("Pokemon Names", names )

table.add_column("Type", ["Electric", "Chomu", "Fire"])

table.align = "l"
print(table)






