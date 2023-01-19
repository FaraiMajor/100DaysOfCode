from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day24/snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}",
                   align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day24/snake_game/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!!",
    #                align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
