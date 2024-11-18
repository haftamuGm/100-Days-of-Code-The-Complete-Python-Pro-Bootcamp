from turtle import Turtle,Screen
hafi=Turtle()
screen=Screen()
screen.listen()
def forward():
    hafi.forward(10)
def backward():
    hafi.backward(30)
def counter_clockwise():
    hafi.left(10)
def clockwise():
    hafi.right(10)
def clear():
    hafi.clear()
    hafi.penup()
    hafi.home()
    hafi.pendown()
screen.onkey(forward,'w')
screen.onkey(backward,'s')
screen.onkey(counter_clockwise,'a')
screen.onkey(clockwise,'d')
screen.onkey(clear,'c')
screen.exitonclick()