from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)

user_bet = screen.textinput("Make your bet.", "Which turtle will win the race? Enter your color : ")

colors = ['red','yellow','orange','blue','green','purple']
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-230, y_pos[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tt in all_turtles:
        if tt.xcor() > 230:
            is_race_on = False
            winning_color = tt.pencolor()
            if winning_color == user_bet:
                print(f"You have won!! The {winning_color} turtle is the winner!!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!!")

        rand_distance = random.randint(0, 10)
        tt.forward(rand_distance)

screen.exitonclick()