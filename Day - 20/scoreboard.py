from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.goto(-20,280)
        self.color('white')
        self.food_eaten()
        self.hideturtle()

    def food_eaten(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, align='center', font=('Arial', 12, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align='center', font=('Arial', 12, 'bold'))