"""
Create a car object so we can store more attributes about the type of threat represented by the car

"""
from turtle import Turtle

class Car(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.threat = kwargs["threat"]

