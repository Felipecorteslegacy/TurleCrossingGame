from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.reset_turtle()
        self.setheading(90)

    def move_up(self):
        current_y = self.ycor()
        self.goto(0, current_y + MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False


