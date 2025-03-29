from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cordinate):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1, 1)
        self.goto(cordinate)

    def move_up(self):
        if self.ycor() < 250:
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)

    def move_down(self):
        if self.ycor() > -250:
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)