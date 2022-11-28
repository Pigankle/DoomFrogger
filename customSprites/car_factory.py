"""Car Factory...> Makes Cars and puts them where they belong."""
from random import randint
import arcade
from customSprites.carbinger import Carbinger
from configuration.constants import CAR_TYPES, RESOURCE_DIR, SCREEN_HEIGHT, SCREEN_WIDTH, CAR_SCALE


class CarFactory:
    def build_car():
        """Create a new random carbinger at a random side of the board."""
        ind = randint(0, len(CAR_TYPES) - 1)
        new_car = Carbinger()
        new_car.objecttype = CAR_TYPES[ind].objecttype
        new_car.color = CAR_TYPES[ind].color
        new_car.speed = -CAR_TYPES[ind].speed
        new_car.cooldown = -1
        new_x = SCREEN_WIDTH
        texture1 = arcade.load_texture(RESOURCE_DIR / CAR_TYPES[ind].icon)
        # Start half the cars on the left side of the screen
        leftside = randint(0, 1)
        if leftside:
            new_x = 0
            new_car.speed = CAR_TYPES[ind].speed
            texture1 = arcade.load_texture(RESOURCE_DIR / CAR_TYPES[ind].icon, mirrored=True)
        new_car.texture = texture1
        new_car.center_x = new_x
        new_car.center_y = randint(40, SCREEN_HEIGHT - 40)
        new_car.angle = 0
        new_car.size = CAR_SCALE
        return new_car
