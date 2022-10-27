"""
Car Manager...>Manages Cars
"""
from random import choice, randint
#from turtle import Turtle
from carbinger import Carbinger
import pandas as pd
from constants import *
from arcade.color import *


class CarManager:
    def new_car():
        """create a new car at the edge of the board"""
        # Get random threat
        ind = randint(0, len(CAR_TYPES) - 1)
        new_car = Carbinger()
        new_car.threat = CAR_TYPES[ind].threat
        new_car.color = CAR_TYPES[ind].color
        new_car.speed  = CAR_TYPES[ind].speed

        rightside = randint(0,1)
        new_x = 0
        new_angle = 180
        new_y = randint(25,SCREEN_HEIGHT - 25)
        if rightside:
            new_x = SCREEN_WIDTH
            new_angle = 0
            new_car.speed = -CAR_TYPES[ind].speed
        new_car.center_x = new_x
        new_car.center_y= new_y
        new_car.angle= new_angle
        new_car.size = CAR_SCALE
        return new_car
