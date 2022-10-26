"""
Create the player's turtle

"""
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_COLOR = "green"

class Player(Turtle):
    """Handles creation of turtle and moving the turtle"""
    def __init__(self):
        """
        Create a turtle at the fixed starting position
        """
        super().__init__()
        self.shape("turtle")
        self.color(TURTLE_COLOR)
        self.penup()
        self.setposition(STARTING_POSITION)

    def go_heading(self, angle, dist):
        """ Move turtle dist pixels in the direction of angle"""
        self.seth(angle)
        self.forward(dist)
