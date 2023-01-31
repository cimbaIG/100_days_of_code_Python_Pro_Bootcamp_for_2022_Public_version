import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_starting_positions = [0, 50, 100, 150, 200, 250]

# Create turtle objects of different colors and position them to the starting positions
turtles = list()
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230,y=-100+turtle_starting_positions[i])

# Simulate race by using while loop and for loop.
keep_racing = True
while keep_racing == True:
    for turtle in turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() >= 230:
            keep_racing = False
            if colors[turtles.index(turtle)] == user_bet:
                print(f"You win! {colors[turtles.index(turtle)].capitalize()} turtle has won!")
            else:
                print(f"You lose! {colors[turtles.index(turtle)].capitalize()} turtle has won!")

screen.exitonclick()

# Udemy solution
""" from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick() """