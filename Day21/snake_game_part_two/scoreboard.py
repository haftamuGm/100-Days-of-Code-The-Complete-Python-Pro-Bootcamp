from turtle import Turtle
ALIGNMENT='center'
FONT=("Aerial", 7 * 3, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updated()
    def updated(self):
        self.write(f"score  :{self.score}", move=True, align=ALIGNMENT, font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", move=True, align=ALIGNMENT, font=FONT)
    def increase_by_one(self):
        self.goto(0, 270)
        self.score+=1
        self.clear()
        self.updated()