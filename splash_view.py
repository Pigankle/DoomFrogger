from game_view import GameView
from get_news import request_all_articles, stock_all_articles
from constants import *


class SplashView(arcade.View):
    """ View to show when game is over """

    def __init__(self, *args, **kwargs):
        """ This is run once when we switch to this view """
        super().__init__()
        # Load screenshot of game over state
        self.texture = arcade.load_texture(RESOURCE_DIR / SPLASH_IMAGE)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH * .8, SCREEN_HEIGHT * .8)
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=16, anchor_x="center")

    """
   def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
    """

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Request article text and stored parsed html
        request_all_articles()
        # Find thematic articles from parsed html and save in list
        saved_articles = stock_all_articles(num_articles = NUM_ARTICLES)
        game_view = GameView()
        game_view.setup(articles=saved_articles)
        self.window.show_view(game_view)
