def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:
    if (front_is_clear() == True) and (wall_on_right() == True):
        move()
    elif (wall_on_right() == False) and (right_is_clear() == True):
        turn_right()
        move()
        turn_right()
        move()
    elif wall_in_front() == True:
        turn_left()
    else:
        move()

