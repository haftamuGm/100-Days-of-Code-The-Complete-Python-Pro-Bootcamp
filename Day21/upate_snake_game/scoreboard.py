from turtle import Turtle
ALIGNMENT='center'
FONT=("Aerial", 7 * 3, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=0
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.updated()
    def updated(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score :{self.score}  High Score  :{self.highscore}", move=True, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.updated()
    def increase_by_one(self):
        self.score+=1
        self.updated()