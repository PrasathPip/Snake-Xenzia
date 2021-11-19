from turtle import Turtle
FONT=('Courier', 16, 'bold')
ALIGNMENT="center"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.color("white")
        self.score = 0
        self.print()

    def print(self):
        self.write(arg=f"SCORE : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over", move=False, align="center", font=('Courier', 16, 'bold'))


    def swallowed(self):
        self.score += 1
        self.clear()
        self.print()