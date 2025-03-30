from turtle import Turtle

FONT = ('Arial', 12, 'bold')

def fetch_highscore():
    with open("high_score.txt") as file:
        return int(file.read())

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = fetch_highscore()
        self.penup()
        self.goto(-20,280)
        self.color('white')
        self.food_eaten()
        self.hideturtle()
        self.update_scoreboard()

    def food_eaten(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", False, align='center', font=FONT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, align='center', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
