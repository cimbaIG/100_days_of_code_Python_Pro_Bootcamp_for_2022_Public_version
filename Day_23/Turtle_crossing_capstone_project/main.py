import time
from turtle import Screen
from player import FINISH_LINE_Y
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = list()
cars.append(CarManager())

screen.listen()
screen.onkey(player.move, "space")

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()
        if player.distance(car) < 20: 
            scoreboard.game_over()
            game_is_on = False

    if i % 6 == 0:
        cars.append(CarManager())

    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_score()
        for car in cars:
            car.increase_speed()

    i += 1

screen.exitonclick()