import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

tim.pensize(10)

for n in range(50):
    tim.speed('fast')
    tim.color(random_colors())
    angle = [1,2,3,4]
    tim.right(90 * random.choice(angle))
    tim.forward(30)

screen = Screen()
screen.exitonclick()