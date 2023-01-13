import random
from turtle import *
background = 'day19/racetrack.png'

screen = Screen()
screen.setup(width=848, height=1261)
screen.bgpic(background)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


y_start = 550
all_turtles = []
for i in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-385, y=y_start)
    all_turtles.append(new_turtle)
    y_start -= 220

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You've guessed correct! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"Oops! You've lost. The {winning_color} turtle is the winner 🙃")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.mainloop()
