from turtle import Screen, Turtle, colormode
import random


tim = Turtle()
tim.hideturtle()
tim.pen(pensize=1)
tim.speed(11)
# tim.shape('turtle')
# tim.color("gold4")

########### Challenge 1 - Star with star corners ########
tim.begin_fill()
for _ in range(5):
    tim.forward(-300)
    tim.right(144)
    for _ in range(5):
        tim.forward(50)
        tim.right(144)
        tim.fillcolor("gold4")

tim.end_fill()

########### Challenge 2 - Dashed Line ########
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Change Color function


def change_color():
    colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.color(R, G, B)


########### Challenge 3 - Different Shapes ########
sides = 3
angle = 0
while sides < 10:
    change_color()
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

    sides += 1

########### Challenge 4 - Random Walk ########

angles = [0, 90, 180, 270]

for _ in range(100):
    change_color()
    tim.forward(25)
    tim.right(random.choice(angles))


########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        change_color
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# alternative
for _ in range(0, 100):
    change_color()
    tim.circle(75)
    tim.left(5)


print(tim)

screen = Screen()
# screen.bgcolor('black')
screen.mainloop()
