from turtle import Turtle

UP_BOUNDARY = 230
DOWN_BOUNDARY = -230

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y_cor = self.ycor() + 20
        if new_y_cor < UP_BOUNDARY:
            self.goto(self.xcor(), new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        if new_y_cor > DOWN_BOUNDARY:
            self.goto(self.xcor(), new_y_cor)