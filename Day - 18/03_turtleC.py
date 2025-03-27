from turtle import Turtle, Screen
import random

tim = Turtle()

colors_list = ['sandy brown','plum','crimson','indigo','maroon','pale violet red','dark olive green','yellow','sea green','dark blue','dodger blue']
def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(random.choice(colors_list))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for n in range(3,11):
    draw_shape(n)

screen = Screen()
screen.exitonclick()