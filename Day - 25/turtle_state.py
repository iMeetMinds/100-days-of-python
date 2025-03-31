from turtle import Turtle
FONT = ('Arial', 10, 'bold')

class StatePrint(Turtle):

    def __init__(self, x, y, state_name):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write(f"{state_name}", False, "Center", font=FONT)
