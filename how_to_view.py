from game_view import GameView
import splash_view
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import fading_view as fv
import arcade


class HowToView(fv.FadingView):
    """Class to manage the game overview."""

    def on_update(self, dt):
        self.update_fade(next_view=self.next_view)

    def on_show_view(self):
        """Call when switching to this view."""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """Draw the game over view."""
        self.clear()
        self.howtext.draw()
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """If user hits a key, go back to the main menu view."""
        if key in []:
            self.next_view = GameView
        else:
            self.next_view = splash_view.SplashView
        self.fade_out = 0

    def setup(self):
        """Set up how to view."""
        # Replace 'pass' with the code to set up your game
        self.next_view = GameView
        self.howtext = arcade.Text(
            "Use Arrow keys to avoid bad news."
            "\nCollect roses to distract yourself."
            "\nYou'll eventually die.\n"
            "\nClick or press an arrow key to begin game\n"
            "\nPress any other key to return to splash",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT * 0.75,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            multiline=True,
            width=SCREEN_WIDTH / 1.25,
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Click mouse to go back to Game View."""
        self.next_view = GameView
        if self.fade_out is None:
            self.fade_out = 0
