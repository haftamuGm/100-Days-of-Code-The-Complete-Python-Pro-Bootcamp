import time
from turtle import Screen
from player import Player
from car_manager import Carmanager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
player=Player()
car_manager=Carmanager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.up,'Up')
screen.tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.ycor()>=280:
        player.level_finished()
        car_manager.level_up()
        scoreboard.levelup()
    for car in car_manager.cars:
        if player.distance(car)<20:
            game_is_on=False
            scoreboard.Gameover()


screen.exitonclick()

