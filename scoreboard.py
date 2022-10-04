from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.level_score()

    def game_over(self):
        self.color("black")
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def level_score(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-230, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL : {self.level} ", align="center", font=("courier", 15, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
