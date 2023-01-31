from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")

""" i = 0
while i < 4:
    my_turtle.forward(100)
    my_turtle.right(90)
    i += 1
 """
for i in range(0,4):
    my_turtle.forward(100)
    my_turtle.right(90)

my_screen = Screen()
my_screen.exitonclick()