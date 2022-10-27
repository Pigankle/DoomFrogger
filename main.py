"""
A simplified game of Frogger
"""
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from get_news import get_article
from display import DisplayText
#from scoreboard import Scoreboard

# Define font parameters
FONT = ("Arial", 14, "bold")
STARTING_CAR_COUNT = 15
PLAYER_STEP_DIST = 10
screen = Screen()
screen.setup(width=600, height=600)
carMan = CarManager()
resultsDisplay = DisplayText()

for i in range(STARTING_CAR_COUNT):
    carMan.new_car()
screen.tracer(0)

# TODO MAKE SAFE ZONES

player1 = Player()
screen.onkeypress(lambda heading=90:  player1.go_heading(heading, PLAYER_STEP_DIST), "Up")
screen.onkeypress(lambda heading=270: player1.go_heading(heading, PLAYER_STEP_DIST), "Down")
screen.onkeypress(lambda heading=180: player1.go_heading(heading, PLAYER_STEP_DIST), "Left")
screen.onkeypress(lambda heading=000: player1.go_heading(heading, PLAYER_STEP_DIST), "Right")
screen.listen()
game_is_on = True

while game_is_on:
    screen.update()
    carMan.advance_cars()
    for car in carMan.carlist:
        if player1.distance((car.position())) < 10:
            # Format threat string
            threatType = car.threat.replace("_", " ").upper()
            # Get article related to the threat
            article = get_article(car.threat)
            # Display type of threat
            player1.write(arg=f'THREAT: {threatType}\n', font=FONT)
            # Get first part of article text
            article_text1 = article["text"][0:80]
            # Display game over message with article text
            resultsDisplay.text_at_xy(-290, 0, f'Game Over!\n{article_text1}[...]\n') 
            game_is_on = False
    sleep(0.05)

screen.exitonclick()
