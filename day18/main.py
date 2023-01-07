from turtle import Screen, Turtle


tim = Turtle()
tim.hideturtle()
tim.pen(pencolor="gold", pensize=3)
# tim.shape('turtle')
tim.color("gold4")

tim.begin_fill()
for _ in range(5):
    tim.forward(-300)
    tim.right(144)
    for _ in range(5):
        tim.forward(50)
        tim.right(144)
        tim.fillcolor("gold4")

tim.end_fill()
tim.speed("slow")

for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()

print(tim)

screen.bgcolor('black')
screen.mainloop()
