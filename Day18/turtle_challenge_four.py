from turtle import Turtle
import random
tim=Turtle()
tim.pensize(7) # this to increase the draw line size
tim.speed('fastest')
color = ["cyan", "magenta", "lime", "teal", "gold", "indigo", "violet", "salmon"]
direction=[0,90,180,270]

for _ in range(200):
    tim.color(random.choice(color)) #to generate random number
    tim.forward(30)
    tim.setheading(random.choice(direction))

