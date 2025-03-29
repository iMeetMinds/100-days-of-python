from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, False, align='center', font=('Courier', 40, 'bold'))
        self.goto(100, 230)
        self.write(self.r_score, False, align='center', font=('Courier', 40, 'bold'))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner_pop(self):
        if self.l_score >= 5:
            self.goto(0, 0)
            self.write("Left player won!!", False, align='center', font=('Courier', 40, 'bold'))
        if self.r_score >= 5:
            self.goto(0, 0)
            self.write("Right player won!!", False, align='center', font=('Courier', 40, 'bold'))