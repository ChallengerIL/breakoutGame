from turtle import Turtle


class Paddle(Turtle):

    STRETCH_WID = 10

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=self.STRETCH_WID, stretch_len=1)
        self.color("white")
        self.goto(0, -250)
        self.setheading(90)
        self.width = width
        self.height = height

    # Legacy code, move with arrow keys
    def move_left(self):
        if self.xcor() - self.STRETCH_WID * 11.5 > -self.width / 2:
            new_x = self.xcor() - 30
            self.goto(new_x, self.ycor())

    # Legacy code, move with arrow keys
    def move_right(self):
        if self.xcor() + self.STRETCH_WID * 12 < self.width / 2:
            new_x = self.xcor() + 30
            self.goto(new_x, self.ycor())

    # Paddle follows mouse movements
    def on_motion(self, event):
        x = event.x - self.width / 2

        # Check for screen boundaries
        if x > - self.width / 2 + self.STRETCH_WID * 10:
            if x < self.width / 2 - self.STRETCH_WID * 11:
                self.goto(x, self.ycor())
