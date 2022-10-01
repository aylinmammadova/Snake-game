from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Food appears each time in random place"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
