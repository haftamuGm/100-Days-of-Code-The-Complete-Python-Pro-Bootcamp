import turtle
from  turtle import Screen,Turtle
from snake import Snake

import time
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')  # Default to white if the input is invalid

screen.title('My Snake Game')
snake=Snake()
screen=Screen()
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

screen.exitonclick()