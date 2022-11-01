from constants import *
from splash_view import SplashView
from game_view import GameView
#from instruction_view import InstructionView


def main():
    """launch a new game window with start_view"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = SplashView()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()