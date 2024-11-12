def turn():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
        turn()
        move()
        turn()
        move()
        turn_left()





