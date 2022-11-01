import arcade
from game_view import GameView
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
                                SCREEN_WIDTH*.8, SCREEN_HEIGHT*.8)
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=16, anchor_x="center")

    """
   def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
    """

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)