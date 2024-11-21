from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x=10
        self.y=10
        self.maxspeed = 0.1
    def move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)

    def y_bounce(self):
        self.y*=-1
    def x_bounce(self):
        self.x*=-1
        self.maxspeed *=0.9
    def refresh(self):
        self.goto(0,0)
        self.max=0.1
        self.x_bounce()