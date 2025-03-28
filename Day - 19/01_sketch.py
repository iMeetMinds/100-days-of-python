from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def tim_forward():
    return tim.forward(10)

def tim_backwards():
    return tim.backward(10)

def tim_clockwise():
    return tim.right(10)

def tim_anti_clockwise():
    return tim.left(10)

def tim_clear():
    return screen.resetscreen()

screen.listen()
screen.onkey(key = 'w', fun = tim_forward)
screen.onkey(key = 's', fun = tim_backwards)
screen.onkey(key = 'd', fun = tim_clockwise)
screen.onkey(key = 'a', fun = tim_anti_clockwise)
screen.onkey(key = 'c', fun = tim_clear)

screen.exitonclick()