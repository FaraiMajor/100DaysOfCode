from turtle import *


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.penup()
        self.goto(new_x, new_y)
