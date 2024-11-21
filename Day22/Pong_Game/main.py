from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()
ball=Ball()
scoreboard=Scoreboard()
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
screen.onkey(left_paddle.goup,'w')
screen.onkey(left_paddle.godown,'s')
screen.onkey(right_paddle.goup,'Up')
screen.onkey(right_paddle.godown,'Down')
screen.tracer(0)
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle) <50 and ball.xcor()>-320:
        ball.x_bounce()
    if ball.xcor()>380:
        ball.refresh()
        scoreboard.leftpont()
    if ball.xcor()<-380:
        ball.refresh()
        scoreboard.rightpoint()



screen.exitonclick()
