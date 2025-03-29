from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('PONG')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

ball = Ball()
sb = ScoreBoard()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        sb.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        sb.r_point()

    if sb.l_score >= 5 or sb.r_score >= 5:
        is_game_on = False
        sb.winner_pop()

screen.exitonclick()