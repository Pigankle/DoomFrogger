"""
Create the player's turtle

"""
import arcade
from constants import *
#from turtle import Turtle

class Player(arcade.Sprite):
    def __init__(self):
        """
        Create a turtle at the fixed starting position
        """
        super().__init__()
        self.texture = arcade.load_texture(RESOURCE_DIR / PLAYER_TEXTURE)


# TODO Obsolete code.  Left in as a reference. To be removed when game is functioning

#   # class obs_Player(Turtle):
#   """Handles creation of turtle and moving the turtle"""
#   def __init__(self):
#       """
#       Create a turtle at the fixed starting position
#       """
#       super().__init__()
#       self.shape("turtle")
#       self.color(FROG_COLOR)
#       self.penup()
#       self.setposition(PLAYER_STARTING_POSITION)

#   def go_heading(self, angle, dist):
#       """ Move turtle dist pixels in the direction of angle"""
#       self.seth(angle)
#       self.forward(dist)
