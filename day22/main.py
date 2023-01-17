from turtle import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Turtle()
paddle.goto(350, 0)
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.turtlesize(stretch_wid=5, stretch_len=1)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(350, new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(350, new_y)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.exitonclick()
