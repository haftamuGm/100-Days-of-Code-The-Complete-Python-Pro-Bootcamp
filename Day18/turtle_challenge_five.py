from turtle import Turtle,colormode,Screen
import random
tim=Turtle()
tim.speed('fastest')
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
tim.speed("fastest")
for _ in range(37):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading+10)
    tim.circle(100)
screen=Screen()
screen.exitonclick()

