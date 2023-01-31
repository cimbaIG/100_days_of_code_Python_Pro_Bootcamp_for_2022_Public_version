from turtle import Turtle, Screen
import random

my_turtle = Turtle()

angle = 360
num_of_sides = [3, 4, 5, 6, 7, 8, 9]
colors = ["black", "red", "blue", "green", "yellow", "pink", "brown"]

angles = []
for side in range(0,len(num_of_sides)):
    angles.append(angle/num_of_sides[side])

i = 0
for angle in angles:
    my_turtle.color(random.choice(colors))
    for _ in range(0,num_of_sides[i]):
        my_turtle.forward(100)
        my_turtle.right(angle)
    i += 1

my_screen = Screen()
my_screen.exitonclick()

# Udemy solution
""" import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n) """