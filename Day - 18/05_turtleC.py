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

tim.speed('fastest')

def draw_circle(pos):
    for _ in range(int(360 / pos)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + pos)

draw_circle(5)

screen = Screen()
screen.exitonclick()