def turn():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


