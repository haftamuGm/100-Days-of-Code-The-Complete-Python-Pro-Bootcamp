from turtle import Turtle,colormode
import random
tim=Turtle()
tim.pensize(7) # this to increase the draw line size
tim.speed('fastest')
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
direction=[0,90,180,270]

for _ in range(200):
    tim.color(random_color()) #to generate random number
    tim.forward(30)
    tim.setheading(random.choice(direction))

