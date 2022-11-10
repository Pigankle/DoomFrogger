from game_view import GameView
import splash_view
from get_news import request_all_articles, stock_all_articles
from constants import *
import fading_view  as fv
import config
import arcade

class HowToView(fv.FadingView):
    """ Class to manage the game overview """
    def on_update(self, dt):
        self.update_fade(next_view=self.next_view)

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        self.clear()
        self.howtext.draw()
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ If user hits a key, go back to the main menu view """
        if key in []:
           self.next_view = GameView
        else:
            self.next_view = splash_view.SplashView
        self.fade_out = 0

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        self.next_view = GameView
        self.howtext = arcade.Text("Use Arrow keys to avoid bad news."
                            "\nCollect roses to distract yourself."
                            "\nYou'll eventually die.\n"
                            "\nClick or press an arrow key to begin game\n"
                            "\nPress any other key to return to splash", SCREEN_WIDTH / 2, SCREEN_HEIGHT *.75,
                            arcade.color.WHITE, 20, anchor_x="center", multiline=True, width = SCREEN_WIDTH/1.25)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.next_view = GameView
        if self.fade_out is None :
            self.fade_out = 0