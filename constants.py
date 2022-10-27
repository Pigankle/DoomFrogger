from pathlib import Path
import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Doom Frogger"
PLAYER_CHARACTER_SCALING = 0.1
TILE_SCALING = 0.1
PLAYER_MOVEMENT_SPEED = 5

PLAYER_SPRITE_IMG = "images/FrogSprite.png"
PLAYER_STARTING_POSITION = {"x":300, "y":20}
PLAYER_MOVE_DISTANCE = 5
PLAYER_TEXTURE = "images/FrogSprite.png"
RESOURCE_DIR = Path(__file__).parent

FONT = ("Arial", 14, "bold")

STARTING_CAR_COUNT = 10
CAR_SCALE = .05
CAR_DEFAULT_ICON = "images/carbinger-light.png"
CAR_SPAWN_RATE = 2
MAX_CAR_CT = 25

@dataclass
class car_spec:
    threat: str = 'climate_change'
    color: arcade.Color = arcade.color.RED
    speed: float = 6
"""THREATS:"""
#TODO One of the threats should be something like amphibian die off

CAR_TYPES = [car_spec("climate_change", arcade.color.RED, 6),
             car_spec( "famine", arcade.color.BLACK, 1),
             car_spec( "nuclear_war", arcade.color.RAJAH, 5),
             car_spec( "pandemic", arcade.color.BRIGHT_GREEN, 4),
             car_spec( "machine_superintelligence", arcade.color.BRIGHT_NAVY_BLUE, 3),
             car_spec( "crop_failure", arcade.color.BOYSENBERRY, 2)]

#Horseman icon source: https://www.pngegg.com/en/png-cevbs