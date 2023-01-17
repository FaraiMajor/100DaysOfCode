from turtle import *


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.goto(position)
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.get_x = self.xcor()
        self.new_y = self.ycor() + 20
        self.goto(self.get_x, self.new_y)

    def down(self):
        self.get_x = self.xcor()
        self.new_y = self.ycor() - 20
        self.goto(self.get_x, self.new_y)
