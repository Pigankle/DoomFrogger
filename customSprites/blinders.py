"""Create a blinder object."""
from random import uniform, randint
import arcade
from configuration.constants import RESOURCE_DIR, BLINDER_DEFAULT_ICON, BLINDER_SCALE, SCREEN_HEIGHT, SCREEN_WIDTH


class Blinder(arcade.Sprite):
    """Create a new blinder at a random position on the screen."""

    def __init__(self, *args, **kwargs):
        super().__init__(RESOURCE_DIR / BLINDER_DEFAULT_ICON, BLINDER_SCALE)
        self.speed = randint(1, 3)
        self.center_x = uniform(25, SCREEN_WIDTH - 25)
        self.center_y = uniform(25, SCREEN_HEIGHT - 25)
        self.move_dir = [uniform(-1, 1), uniform(-1.0, 1)]
        self.objecttype = "Blinder"

    def blinder_move(self):
        """Move blinder."""
        self.center_x += self.move_dir[0] * self.speed
        self.center_y += self.move_dir[1] * self.speed
