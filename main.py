from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import BricksLayer
from scoreboard import Scoreboard

WIDTH = 850
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)
bricks_layer = BricksLayer(WIDTH, HEIGHT)
scoreboard = Scoreboard()

# Use arrow keys
# screen.listen()
# screen.onkey(paddle.move_left, "Left")
# screen.onkey(paddle.move_right, "Right")

# Use mouse movements
screen.getcanvas().bind("<Motion>", paddle.on_motion)

active = True

while active:
    # detect bounce off of the paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -HEIGHT / 2 + 60:
        ball.y_heading *= -1

    if bricks_layer.hit_check(ball.xcor(), ball.ycor()):
        ball.y_heading *= -1
        scoreboard.add_score(bricks_layer.last_value)

    if ball.missed:
        scoreboard.take_life()

    ball.move()
    screen.update()

    if scoreboard.lives < 1:
        active = False

screen.exitonclick()
