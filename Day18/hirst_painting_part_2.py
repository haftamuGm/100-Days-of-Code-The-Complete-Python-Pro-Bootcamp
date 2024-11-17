import random
from turtle import Turtle,Screen,colormode

color=[(241, 226, 234), (224, 231, 241), (223, 238, 230), (190, 161, 127), (130, 91, 66), (142, 166, 182), (185, 147, 161), (67, 102, 127), (130, 76, 92), (140, 174, 160), (17, 29, 51), (51, 25, 15), (56, 20, 33), (66, 114, 95), (214, 202, 145), (162, 146, 65), (17, 43, 29), (218, 176, 189), (114, 36, 51), (168, 103, 121), (119, 38, 28), (84, 152, 133), (165, 207, 194), (175, 106, 94), (224, 177, 168), (29, 86, 62), (40, 56, 103), (179, 187, 214), (84, 145, 156)]
print(len(color))
hafi=Turtle()
hafi.penup()
hafi.hideturtle()
colormode(255)
hafi.setheading(225)
hafi.forward(300)
hafi.setheading(0)
hafi.speed("fastest")
number_of_dot=180
for dot_count in range(1,number_of_dot+1):
    hafi.dot(15,random.choice(color))
    hafi.forward(50)
    if dot_count %10==0:
        hafi.setheading(90)
        hafi.forward(50)
        hafi.setheading(180)
        hafi.forward(500)
        hafi.setheading(0)
screen=Screen()
screen.exitonclick()


