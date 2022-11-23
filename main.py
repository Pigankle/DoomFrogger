import arcade
import ctypes
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from splash_view import SplashView


# from instruction_view import InstructionView


def main():
    """Launch a new game window with start_view."""
    #https://stackoverflow.com/questions/64777654/matplotlib-chart-shrinks-tkinter-window
    ctypes.windll.shcore.SetProcessDpiAwareness(0)
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = SplashView()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()
