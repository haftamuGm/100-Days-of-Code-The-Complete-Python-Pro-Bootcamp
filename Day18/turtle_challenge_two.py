from turtle import Turtle,Screen
tm=Turtle()
screen=Screen()
for _ in range(20):
    tm.forward(5)
    tm.penup()
    tm.forward(5)
    tm.pendown()

screen.exitonclick()


