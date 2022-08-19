from turtle import Turtle


class Ball(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, -width / 2 + 60)
        self.setheading(45)
        self.starting_pace = 2
        self.pace = self.starting_pace
        self.x_heading = 1
        self.y_heading = 1
        self.width = width
        self.height = height
        self.missed = False

    def move(self):
        self.check_bounce()

        new_x = self.xcor() + self.pace * self.x_heading
        new_y = self.ycor() + self.pace * self.y_heading

        self.goto(new_x, new_y)

    # Check if the ball bounced off of the walls or went out of the frame
    def check_bounce(self):
        self.missed = False

        if self.xcor() > self.width / 2 - 20:
            self.x_heading *= -1
        elif self.xcor() < -self.width / 2 + 20:
            self.x_heading *= -1
        elif self.ycor() > self.height / 2 - 10:
            self.y_heading *= -1
        elif self.ycor() < -self.height / 2 + 20:
            self.reset_position()

    def reset_position(self):
        self.missed = True
        self.goto(0, -self.height / 2 + 60)
        self.y_heading *= -1
        self.pace = self.starting_pace
