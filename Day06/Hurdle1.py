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
for i in range(1,7):
    pass_obstacle()
