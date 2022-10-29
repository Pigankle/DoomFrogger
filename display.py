"""
Create a display object so we can format text output
use https://api.arcade.academy/en/development/api_docs/api/text.html?highlight=text

"""
from Arcade import Text
#from turtle import Turtle, Screen

# Define font parameters
FONT = ("Arial", 14, "bold")

# Function to display text output at specified position

class DisplayHitText(Text):  #LOTS TO DO HERE TODO
    def __init__(self):
        pass

class DisplayText():
    def __init__(self):
        self.turtle = Turtle(visible=False)
        self.turtle.speed('fastest')

    def text_at_xy(self, x, y, text):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.write(text, font=FONT)