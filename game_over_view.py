from arcade import View, set_viewport, Text
from display import *
from constants import *
import fading_view as fv
import splash_view as sv
import config

# View for when the game is over
class GameOverView(fv.FadingView):
    """ View to show when game is over """

    def __init__(self, *args, **kwargs):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = kwargs["txtr"]
        self.game_over_text = kwargs["text"]
        self.game_over_xpos = kwargs["xpos"]
        self.game_over_ypos = kwargs["ypos"]
        self.admonishment = arcade.Text(f"You ignored {(~config.df_collision_history['HitType'].str.contains('BLINDER')).sum()}"
                    f" warnings.  Why won't you listen?\n\n"
                    f"Click to try again, press any key to exit.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                    arcade.color.RED, 30, anchor_x="center", multiline=True, width=SCREEN_WIDTH * 0.8)
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_update(self, dt):
        self.update_fade(next_view=sv.SplashView)


    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        display_headline_text(
            text=self.game_over_text,
            xpos=self.game_over_xpos,
            ypos=self.game_over_ypos
        )

        self.admonishment.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        self.next_view = sv.SplashView
        if self.fade_out is None :
            self.fade_out = 0

    def on_key_press(self, key, _modifiers):
        """ If user hits a key, go back to the main menu view """
        arcade.exit()