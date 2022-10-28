"""
Car Factory...> Makes Cars and puts them where they belong.
"""
from random import choice, randint
from carbinger import Carbinger
from constants import *

class CarFactory:
    def new_car():
        """create a new random carbinger at a random side of the board"""
        ind = randint(0, len(CAR_TYPES) - 1)
        new_car = Carbinger()
        new_car.threat = CAR_TYPES[ind].threat
        new_car.color = CAR_TYPES[ind].color
        new_car.speed  = -CAR_TYPES[ind].speed
        new_car.cooldown = -1

        leftside = randint(0,1)
        new_x = SCREEN_WIDTH
        new_angle = 0
        new_y = randint(25,SCREEN_HEIGHT - 25)
        texture1 = arcade.load_texture(RESOURCE_DIR / CAR_DEFAULT_ICON)
        if leftside:
            new_x = 0
            new_car.speed = CAR_TYPES[ind].speed
            texture1 = arcade.load_texture(RESOURCE_DIR /CAR_DEFAULT_ICON, mirrored = True)
        new_car.texture = texture1
        new_car.center_x = new_x
        new_car.center_y= new_y
        new_car.angle= new_angle
        new_car.size = CAR_SCALE
        return new_car
