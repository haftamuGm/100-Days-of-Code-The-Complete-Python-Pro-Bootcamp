
from  turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')  # Default to white if the input is invalid

screen.title(' '*71+'My Snake Game')
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.tracer(0)
Game_is_on=True
while Game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        scoreboard.increase_by_one()
        snake.extend()
        food.refreash()
    if snake.head.xcor()>=298 or snake.head.xcor()<=-298 or snake.head.ycor()<= -298 or snake.head.ycor()>=298:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset()





screen.exitonclick()