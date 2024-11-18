from turtle import Turtle,Screen
import random
screen=Screen()
screen.listen()
screen.setup(width=500,height=400)
is_choose=True
while is_choose:
    user_color_choice=screen.textinput(title='choose background color',prompt="choose your favorite color  from 'pink','black'")
    if user_color_choice in ['black','pink']:
        screen.bgcolor(user_color_choice)
        is_choose=False
user_bet=screen.textinput(title="Make a Bet",prompt='which one turtles will win a race Enter Color ').lower()
color=["red",'orange','yellow','green','blue','purple']
all_turtle=[]
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-230, -100 + 30 * i)
    new_turtle.color(color[i])
    all_turtle.append(new_turtle)
a=1
is_on_race=True
while is_on_race:
    for turtle in all_turtle:
        random_move=random.randint(0,10)
        turtle.forward(random_move)
        if turtle.xcor()>220:
            if user_bet==turtle.color()[0]:
                print(f"You've Won!:{turtle.pencolor()}")
            else:
                print(f"You've loss :The {turtle.pencolor()} Turtle Win ")
            is_on_race=False



screen.exitonclick()
