import colorgram
from turtle import Turtle, Screen
import random
import turtle

# colors = colorgram.extract('image.jpg', 30)
# color_tuple = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     color_tuple.append(rgb_color)
#
# print(color_tuple)

color_palate = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]

tim = Turtle()
turtle.colormode(255)
turtle.hideturtle()
tim.penup()
x_pos = -300
y_pos = -300
tim.setposition(x_pos, y_pos)
tim.speed('fastest')

for _ in range(10):
    move_pos = 50
    for _ in range(10):
        tim.pendown()
        tim.dot(30, random.choice(color_palate))
        tim.penup()
        tim.forward(move_pos)
    y_pos += move_pos
    tim.setposition(x_pos,y_pos)


screen = Screen()
screen.exitonclick()