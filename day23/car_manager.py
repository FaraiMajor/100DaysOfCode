from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.make_car()

    def make_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
