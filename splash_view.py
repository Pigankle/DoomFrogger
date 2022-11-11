import arcade
from game_view import GameView
from get_news import request_all_articles, stock_all_articles
from constants import *
import fading_view as fv
import config
from how_to_view import HowToView

class SplashView(fv.FadingView):
    """ View to show when game is over """

    def __init__(self, *args, **kwargs):
        #This is run once when we switch to this view
        super().__init__()
        # Load screenshot of game over state
        self.texture = arcade.load_texture(RESOURCE_DIR / SPLASH_IMAGE)
        if len(config.saved_articles) == 0:
            # Request article text and stored parsed html
            request_all_articles()
            # Find thematic articles from parsed html and save in list
            config.saved_articles = stock_all_articles(num_articles=NUM_ARTICLES)
        self.next_view = GameView
    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH * .8, SCREEN_HEIGHT * .8)
        arcade.draw_text("Click to advance   *    Space for Guidance", SCREEN_WIDTH / 2, SCREEN_HEIGHT -2 *16,
                         arcade.color.GRAY, font_size=16, anchor_x="center")
        self.draw_fading()

    def on_update(self, dt):
        self.update_fade(next_view=self.next_view)

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. """
        if self.fade_out is None and key == arcade.key.SPACE:
            self.next_view = HowToView
            self.fade_out = 0

    def setup(self):
        """ This should set up your game and get it ready to play """
        self.texture = arcade.load_texture(RESOURCE_DIR / SPLASH_IMAGE)


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.fade_out is None :
            self.fade_out = 0
