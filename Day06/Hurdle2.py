def turn():
    turn_left()
    turn_left()
    turn_left()
    move()


def pass_obstacle():
    move()
    turn_left()
    move()
    turn()
    turn()
    turn_left()


while at_goal() != True:
    pass_obstacle()

