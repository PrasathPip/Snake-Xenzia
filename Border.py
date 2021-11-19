from turtle import Turtle

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, -280)

    def square(self):
        self.pendown()
        self.goto(-280, 280)
        self.goto(280, 280)
        self.goto(280, -280)
        self.goto(-280, -280)
        self.penup()
