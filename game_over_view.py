from arcade import View, set_viewport
from display import display_text
from constants import *

# View for when the game is over
class GameOverView(View):
    """ View to show when game is over """

    def __init__(self, *args, **kwargs):
        """ This is run once when we switch to this view """
        super().__init__()
        # Load screenshot of game over state
        self.texture = kwargs["image"]#arcade.load_texture(GAME_OVER_IMAGE_PATH)
        self.game_over_text = kwargs["text"]
        self.game_over_xpos = kwargs["xpos"]
        self.game_over_ypos = kwargs["ypos"]
        self.final_screen = kwargs["image"]

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        display_text(
          text=self.game_over_text,
          xpos=self.game_over_xpos,
          ypos=self.game_over_ypos
        )

    #def on_mouse_press(self, _x, _y, _button, _modifiers):
    #    """ If the user presses the mouse button, re-start the game. """
    #    game_view = GameView() TODO: figure out how to do this without circular import
    #    game_view.setup()
    #    self.window.show_view(game_view)