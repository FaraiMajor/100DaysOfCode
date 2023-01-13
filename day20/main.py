from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)


start_new = [(0, 0), (-10, 0), (-20, 0)]

segments = []

for position in start_new:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.shapesize(0.5, 0.5, 0)
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()
