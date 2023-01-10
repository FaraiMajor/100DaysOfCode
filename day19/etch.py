import turtle as t
import random

tim = t.Turtle()

screen = t.Screen()
screen.listen()


def counter_clockwise():
    # tim.circle(-50, 10)
    tim.left(10)


def clockwise():
    # tim.circle(50, 10)
    tim.right(10)


def backwards():
    tim.backward(10)


def forwards():
    tim.forward(10)


def clear():
    tim.reset()


# This will call the up function if the "Left" arrow key is pressed
screen.onkey(counter_clockwise, "Up")
screen.onkey(clockwise, "Down")
screen.onkey(backwards, "Left")
screen.onkey(forwards, "Right")
screen.onkey(clear, "c")


screen.mainloop()  # This will make sure the program continues to run
