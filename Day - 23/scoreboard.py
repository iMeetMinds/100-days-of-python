from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {self.score}", False, align='center', font=FONT)

    def level_update(self):
        self.score += 1
        self.update_scoreboard()

    def winner_pop(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align='center', font=FONT)
