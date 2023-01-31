import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

angle = 3
i = 0
while i < 360:
    t.color(random_color())
    t.speed("fastest")
    t.circle(100)
    t.left(angle)
    i += angle

my_screen = t.Screen()
my_screen.exitonclick()

# Udemy solution
""" def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5) """