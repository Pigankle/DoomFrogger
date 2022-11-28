"""
Create the player's turtle
"""
import arcade
import math
import pandas as pd
from time import time
from configuration.constants import (
    RESOURCE_DIR,
    PLAYER_TEXTURE,
    PLAYER_STARTING_POSITION,
    PLAYER_SPRITE_IMG,
    BLINDER_CT_START,
    PLAYER_CHARACTER_SCALING,
    PLAYER_MOVEMENT_SPEED,
    UPDATES_PER_FRAME,
)

from configuration import config


class Player(arcade.Sprite):
    def __init__(self):
        """Create a turtle at the fixed starting position."""
        super().__init__()
        self.texture = arcade.load_texture(RESOURCE_DIR / PLAYER_TEXTURE)
        self.filename = PLAYER_SPRITE_IMG
        self.center_x = PLAYER_STARTING_POSITION["x"]
        self.center_y = PLAYER_STARTING_POSITION["y"]
        self.scale = PLAYER_CHARACTER_SCALING
        self.is_moving = False
        self.blinder_count = BLINDER_CT_START
        config.df_collision_history = pd.DataFrame()
        # ANIMATION
        self.cur_texture = 1
        # Load Textures
        filename0 = RESOURCE_DIR / "images/FrogSprite_moveL.png"
        filename1 = RESOURCE_DIR / "images/FrogSprite_moveR.png"
        self.walk_textures = [
            arcade.load_texture(filename0),
            arcade.load_texture(filename0),
            arcade.load_texture(filename1),
            arcade.load_texture(filename1),
        ]

    def move_keydown(self, direction):
        """Behavior when a key is pressed down"""
        match direction:
            case (arcade.key.UP):
                self.change_y = PLAYER_MOVEMENT_SPEED
                self.angle = 90
            case (arcade.key.DOWN):
                self.change_y = -PLAYER_MOVEMENT_SPEED
                self.angle = 270
            case (arcade.key.LEFT):
                self.change_x = -PLAYER_MOVEMENT_SPEED
                self.angle = 180
            case (arcade.key.RIGHT):
                self.change_x = PLAYER_MOVEMENT_SPEED
                self.angle = 0
        self.is_moving = True

    def move_keyup(self, direction):
        """Behavior when a key is released"""
        match direction:
            case (arcade.key.UP):
                self.change_y = 0
            case (arcade.key.DOWN):
                self.change_y = 0
            case (arcade.key.LEFT):
                self.change_x = 0
            case (arcade.key.RIGHT):
                self.change_x = 0
        self.is_moving = False

    def fix_orientation(self):
        """Correct orientation when multiple keys have been pressed/released at once."""
        if self.change_x == 0:
            if self.change_y < 0:
                self.angle = 270
            elif self.change_y > 0:
                self.angle = 90
        else:
            heading = math.atan(self.change_y / self.change_x)
            self.angle = math.degrees(heading)
            if self.change_x < 0:
                self.angle -= 180

    def update_animation(self):
        """Animate the frog sprite as it moves around the screen."""
        self.fix_orientation()
        if self.velocity[0] != 0 or self.velocity[1] != 0:
            self.is_moving = True
        if self.is_moving:
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            self.texture = self.walk_textures[frame]

    def update_history(self, nf, os_bl_count, nf_count, txt):
        config.df_collision_history = pd.concat(
            [
                config.df_collision_history,
                pd.DataFrame(
                    {
                        "Time": time(),
                        "HitType": nf.objecttype,
                        "PosX": self.center_x,
                        "PosY": self.center_y,
                        "PrevBlinderCount": self.blinder_count,
                        "onscreen_bl_count": os_bl_count,
                        "Onscreen_Car_count": nf_count,
                        "Text": txt,
                    },
                    index=[0],
                ),
            ]
        )
