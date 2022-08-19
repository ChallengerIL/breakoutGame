from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.lives = 4

        self.update()

    # Update Scoreboard
    def update(self):
        self.clear()

        self.goto(-75, 180)
        self.write(self.lives, align="center", font=("Courier", 80, "normal"))
        self.goto(75, 180)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def take_life(self):
        self.lives -= 1
        self.update()

    def add_score(self, score):
        self.score += score
        self.update()
