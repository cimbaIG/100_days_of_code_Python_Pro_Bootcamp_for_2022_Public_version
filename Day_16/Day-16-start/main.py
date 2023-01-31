""" from turtle import Turtle, Screen

# Create object timmy of class Turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("black", "bisque4")
timmy.forward(100)

# Create object my_screen of class Screen
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() """

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)