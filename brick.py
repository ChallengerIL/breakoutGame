from turtle import Turtle


class Brick(Turtle):

    VALUES = {"red": 7, "orange": 5, "green": 3, "yellow": 1}

    def __init__(self, pos: tuple, color, width):
        super().__init__()
        # Assign Bricks destruction value
        self.value = self.VALUES[color]
        self.penup()
        self.color(color)
        self.goto(pos)
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=width, stretch_len=1)


class BricksLayer:

    COLORS = ["red", "orange", "green", "yellow"]

    def __init__(self, width, height):
        self.bricks = list()
        self.bricks_num = 13
        # Gap in-between the bricks
        self.gap = 4
        # Calculate the bricks' size that can fit into the screen's width
        self.layer_width = width - self.bricks_num - self.bricks_num * self.gap
        self.brick_width = round(self.layer_width / (self.bricks_num * 20))
        self.start_x = -(width / 2) + self.gap + 34
        self.current_x = self.start_x
        self.current_y = height / 4
        self.last_value = 0

        self.build_layer()

    def build_layer(self):
        # Iterate over colors
        for color in self.COLORS:
            # Create bricks for the current layer
            for i in range(self.bricks_num):
                # Keep track of the bricks by adding them to the list of available bricks
                self.bricks.append(Brick((self.current_x, self.current_y), color, self.brick_width))
                # Shift position on the x-axis for the next brick
                self.current_x += self.brick_width * 20 + self.gap

                # Shift position to the beginning if we added the last brick for the current row
                if i == self.bricks_num-1:
                    self.current_x = self.start_x

            # Shift position on the y-axis for the next layer
            self.current_y -= 30 - self.gap

    # Check if brick got hit by ball
    def hit_check(self, ball_x, ball_y):
        # Iterate over bricks available
        for brick in self.bricks:
            # If the distance between the brick and the ball is small enough
            if brick.distance(ball_x, ball_y) < 30:
                # Remove the brick from the list of bricks left
                self.bricks.remove(brick)
                # Record it's value
                self.last_value = brick.value
                # Delete the brick
                brick.reset()
                return True

