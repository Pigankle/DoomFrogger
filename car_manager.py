"""
Car Manager...>Manages Cars
"""
from random import choice, randint
from turtle import Turtle
from car import Car
import pandas as pd

# Define types of threats and associated colors and speeds
THREATS = ["climate_change", "famine", "nuclear_war", "pandemic", "machine_superintelligence", "crop_failure"]
COLORS = ["red", "black", "orange", "green", "blue", "purple"]
SPEEDS = [12, 14, 10, 8, 6, 4]
COLORS_SPEEDS = pd.DataFrame({"threat": THREATS, "color": COLORS, "speed": SPEEDS})

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_RATE = 3
MAX_CAR_CT = 50

class CarManager:
    """
    Responsible for creating new cars, moving them across the screen,
    and keeping a list of how many cars there are
    """
    def __init__(self):
        self.carlist = []

    def advance_cars(self):
        """
        Move all cars across the screen a distance of MOVE_INCREMENT
        If a car moves beyong the boundaries of the game, it is removed and replaced
        with SPAWN_RATE new ones in random positions, up to a total of MAX_CAR_CT
        """
        for car in reversed(self.carlist):
            car.forward(COLORS_SPEEDS.loc[COLORS_SPEEDS["color"] == car.color()[0], "speed"].values[0] // 2)
            if abs(car.xcor() )>305:
                self.carlist.remove(car)
                if len(self.carlist) < MAX_CAR_CT:
                    [f() for f in [self.new_car]*SPAWN_RATE]

    def new_car(self):
        """create a new car at the edge of the board"""
        # Get random threat
        new_threat = choice(THREATS)
        new_car = Car(threat=new_threat)
        new_car.shape("arrow")
        new_car.color(COLORS_SPEEDS.loc[COLORS_SPEEDS["threat"] == new_threat, "color"].values[0])
        new_car.penup()
        new_car.speed(9)
        rightside = randint(0,1)
        new_x = -300
        new_h = 0
        new_y = randint(-270,270)
        if rightside:
            new_x = 292
            new_h = 180
        new_car.setposition(new_x, new_y)
        new_car.seth(new_h)
        self.carlist.append(new_car)
