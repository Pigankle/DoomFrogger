"""
Create a car object so we can store more attributes about the type of threat represented by the car

"""
import math

from constants import *


class Carbinger(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(RESOURCE_DIR / CAR_DEFAULT_ICON, CAR_SCALE)
        self.size = 0
        self.shape = ""
        self.color = (33, 88, 22)
        self.speed = 0

    def car_move(self):
        if abs(self.speed) <= 2:
            ystep = math.sin(10 * math.pi * self.center_x / SCREEN_WIDTH)
            self.angle = math.atan(ystep / self.speed) * 90 / math.pi
            self.center_y += ystep
            if self.center_y < 0:
                self.center_y = 0
            if self.center_y > SCREEN_HEIGHT:
                self.center_y = SCREEN_HEIGHT
        self.center_x += self.speed
