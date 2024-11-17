from turtle import Turtle,Screen
from random import Random
color=['red','green','pink']
mytimy=Turtle()
screen=Screen()
random=Random()

def shape(side):
    for _ in range(side):
        angle=360 / side
        mytimy.color(random.choice(color))
        mytimy.forward(71)
        mytimy.right(angle)

for i in range(3,11):
    shape(i)



