"""
Create a car object so we can store more attributes about the type of threat represented by the car

"""
#from turtle import Turtle
import math
from constants import *

class Carbinger(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(RESOURCE_DIR /CAR_DEFAULT_ICON,CAR_SCALE)
        self.size = 0
        self.shape = ""
        self.color = (33,88,22)
        self.speed = 0

    def update(self):
        super.update()

    def car_move(self):
        if abs(self.speed) <= 2:
            self.center_y += math.sin(10*math.pi*self.center_x/SCREEN_WIDTH)
        self.center_x += self.speed




