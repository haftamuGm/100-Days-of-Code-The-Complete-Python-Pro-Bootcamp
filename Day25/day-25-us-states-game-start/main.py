
from turtle import Turtle,Screen
import pandas
a=Turtle()
a.hideturtle()
a.penup()
screen=Screen()
screen.title("united states")
score=0
user_guesed=[]
x=[]
while len(user_guesed)<50:
    user=screen.textinput(f"{score}/50",prompt="What's Another state name").title()
    screen.bgpic('blank_states_img.gif')
    data=pandas.read_csv("50_states.csv")
    states=data["state"].to_list()
    if user=='Exit':
        for i in states:
            if i not in user_guesed:
                x.append(i)
        unlist={
            "unlist_name":x
        }
        unlist_data=pandas.DataFrame(unlist)
        unlist_data.to_csv("unlist_states.csv")

        break

    if user not in user_guesed and user in states:
        location=data[data.state==user]
        user_guesed.append(user)
        a.goto(location.x.item(),location.y.item())
        a.write(arg=user,align='center',font=("Arial", 7, "normal"))
        score+=1





#screen.exitonclick()