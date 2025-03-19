def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:
    if right_is_clear() == True:
        turn_right()
        if wall_in_front() != True:
            move()
    elif wall_in_front() == True:
        turn_left()
    else:
        move()

