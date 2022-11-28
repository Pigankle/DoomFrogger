import arcade
from configuration.constants import (
    SMOKE_RISE_RATE,
    PARTICLE_FADE_RATE,
    SMOKE_START_SCALE,
    SMOKE_EXPANSION_RATE,
    SMOKE_FADE_RATE,
)


class Smoke(arcade.SpriteCircle):
    """Render a puff of smoke."""

    def __init__(self, size):

        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def update(self):
        """Update this particle."""
        if self.alpha <= PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += SMOKE_EXPANSION_RATE
