from pathlib import Path
import arcade
from dataclasses import dataclass

"""WINDOW PARAMETERS"""
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Doom Frogger"
TILE_SCALING = 0.1
SPLASH_IMAGE = "images/DoomFroggerLogo.png"
"""Text display"""
FONT_SIZE = 16
FONT_COLOR = (255, 255, 255)
TEXT_WIDTH = 200
GAME_OVER_IMAGE_PATH = "images/game_over.png"
RESOURCE_DIR = Path(__file__).parent

""" PLAYER BEHAVIOR"""
PLAYER_MOVE_KEYS = [arcade.key.UP,
                    arcade.key.DOWN,
                    arcade.key.LEFT,
                    arcade.key.RIGHT]
PLAYER_MOVEMENT_SPEED = 5
PLAYER_SPRITE_IMG = "images/FrogSprite.png"
PLAYER_STARTING_POSITION = {"x":300, "y":20}
PLAYER_TEXTURE = "images/FrogSprite.png"
PLAYER_CHARACTER_SCALING = 0.1
UPDATES_PER_FRAME = 5

"""BLINDER BEHAVIOR """
BLINDER_DEFAULT_ICON = "images/rose.png"
BLINDER_SCALE = 0.1
BLINDER_SPAWN_RATE = 0.01
BLINDER_HIT_TEXT_COLOR = arcade.color.RASPBERRY_PINK
BLINDER_HIT_FONT = 'comic'
BLINDER_HIT_TEXT_PERMANENCE = 15
BLINDER_HIT_TEXT_DECAY_RATE = 0.1

"""CARBINGER PARAMETERS"""
STARTING_CAR_COUNT = 1
CAR_SCALE = .05
CAR_DEFAULT_ICON = "images/carbinger-light.png"
CAR_SPAWN_RATE = 2
MAX_CAR_CT = 45
CAR_HIT_TEXT_PERMANENCE = 15
CAR_HIT_TEXT_DECAY_RATE = 0.2


@dataclass
class car_spec:
    threat: str = 'climate_change'
    color: arcade.Color = arcade.color.RED
    speed: float = 6
    icon: str = "images/carbinger-light.png"

"""THREATS:
 Icons should be facing to the left if they have left-right orientation
 Horseman icon source: https://www.pngegg.com/en/png-cevbs
"""
CAR_TYPES = [car_spec("climate_change", arcade.color.RED, 6, CAR_DEFAULT_ICON),
             car_spec( "famine", arcade.color.BLACK, 1, CAR_DEFAULT_ICON),
             car_spec( "nuclear_war", arcade.color.RAJAH, 5, CAR_DEFAULT_ICON),
             car_spec( "pandemic", arcade.color.BRIGHT_GREEN, 4, CAR_DEFAULT_ICON),
             car_spec( "machine_superintelligence", arcade.color.BRIGHT_NAVY_BLUE, 3, CAR_DEFAULT_ICON),
             car_spec( "crop_failure", arcade.color.BOYSENBERRY, 2, CAR_DEFAULT_ICON)]
