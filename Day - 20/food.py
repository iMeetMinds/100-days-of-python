from turtle import Turtle
import random

COLORS = ['red','yellow','orange','blue','green','purple']

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
