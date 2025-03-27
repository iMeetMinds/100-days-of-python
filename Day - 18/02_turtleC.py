from turtle import Turtle, Screen

tim = Turtle()

for _ in range(10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = Screen()
screen.exitonclick()