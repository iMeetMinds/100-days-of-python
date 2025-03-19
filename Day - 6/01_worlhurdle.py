def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


for n in range(1, 7):
    move()
    jump()