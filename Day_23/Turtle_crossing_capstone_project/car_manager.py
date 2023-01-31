from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()
        self.move()

    def create_car(self):
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        x_pos = 300
        y_pos = random.randint(-230, 230)
        self.goto(x_pos, y_pos)

    def move(self):
        self.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
