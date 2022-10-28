"""
Create a car object so we can store more attributes about the type of threat represented by the car

"""
#from turtle import Turtle
import arcade
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





