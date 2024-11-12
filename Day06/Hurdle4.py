def turn():
    turn_left()
    turn_left()
    turn_left()
def jamp():
    turn_left()
    while wall_on_right():
        move()
    turn()
    move()
    turn()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jamp()
    else:
        move()




