from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"LEVEL :{self.level}", align="center", font=FONT)
    def levelup(self):
        self.level +=1
        self.update()
    def Gameover(self):
        self.goto(0,0)
        self.color("black")
        self.write(arg="Game Over ",align="center", font=FONT)