from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_position = random.randint(-260, 260)
        y_position = random.randint(-260, 260)
        self.goto(x_position, y_position)