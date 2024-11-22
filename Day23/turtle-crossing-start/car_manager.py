from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Carmanager():
    def __init__(self):
        self.distance=STARTING_MOVE_DISTANCE
        self.cars=[]
    def create_car(self):
        number_of_cars=random.randint(1,7)
        if number_of_cars==1:
            car=Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.goto(300,random.randint(-250,250))
            self.cars.append(car)
    def move(self):
        for car in self.cars:
            car.backward(self.distance)
    def level_up(self):
        self.distance +=MOVE_INCREMENT

