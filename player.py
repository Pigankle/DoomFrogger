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
        self.filename = PLAYER_SPRITE_IMG
        self.center_x = PLAYER_STARTING_POSITION["x"]
        self.center_y = PLAYER_STARTING_POSITION["y"]
        self.scale = PLAYER_CHARACTER_SCALING

    def move_keydownd(self, direction):
        match direction:
            case "up":
                self.change_y = PLAYER_MOVEMENT_SPEED
                self.angle = 0

    def move_keydown(self, direction):
        match direction:
            case (arcade.key.UP):
                self.change_y = PLAYER_MOVEMENT_SPEED
                self.angle = 0
            case (arcade.key.DOWN):
                self.change_y = -PLAYER_MOVEMENT_SPEED
                self.angle = 180
            case (arcade.key.LEFT):
                self.change_x = -PLAYER_MOVEMENT_SPEED
                self.angle = 90
            case (arcade.key.RIGHT):
                self.change_x = PLAYER_MOVEMENT_SPEED
                self.angle = 270
    def move_keyup(self, direction):
        match direction:
            case (arcade.key.UP):
                self.change_y = 0
            case (arcade.key.DOWN):
                self.change_y = 0
            case (arcade.key.LEFT):
                self.change_x = 0
            case (arcade.key.RIGHT):
                self.change_x = 0

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
