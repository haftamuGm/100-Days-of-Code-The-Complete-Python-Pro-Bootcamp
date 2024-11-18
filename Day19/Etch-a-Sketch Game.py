from turtle import Turtle,Screen
import random
hafi=Turtle()
def forward():
    hafi.forward(10)
def backward():
    hafi.backward(10)
def counter_clockwise():
    hafi.left(10)
def clockwise():
    hafi.right(10)
def clear():
    hafi.penup()
    hafi.clear()
    hafi.home()
    hafi.pendown()
screen=Screen()
screen.listen()
screen.onkey(key='w',fun=forward)
screen.onkey(key='s',fun=backward)
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear)
screen.exitonclick()
