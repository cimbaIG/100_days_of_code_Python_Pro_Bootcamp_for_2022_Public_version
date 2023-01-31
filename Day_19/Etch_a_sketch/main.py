from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def move_counter_clockwise():
    my_turtle.left(10)

def move_clockwise():
    my_turtle.right(10)

def clear_drawing():
    my_turtle.penup()
    my_turtle.home()
    my_turtle.clear()
    my_turtle.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()