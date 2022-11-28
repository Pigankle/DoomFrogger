import arcade

from random import uniform
from arcade import get_image
from time import time

from configuration import config
import views.fading_view as fading_view
from customSprites import player
from customSprites.car_factory import CarFactory
from newsTextAndPlots.get_news import replenish_articles
from newsTextAndPlots import display
from views.game_over_view import GameOverView
from configuration.constants import (
    TILE_SCALING,
    SCREEN_HEIGHT,
    STARTING_CAR_COUNT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    MAX_CAR_CT,
    CAR_SPAWN_RATE,
    PARTICLE_COUNT,
    CAR_HIT_TEXT_PERMANENCE,
    CAR_HIT_TEXT_DECAY_RATE,
    BLINDER_HIT_TEXT_DECAY_RATE,
    BLINDER_HIT_TEXT_PERMANENCE,
    BLINDER_HIT_TEXT_COLOR,
    BLINDER_SPAWN_RATE,
    RESOURCE_DIR,
)
from customSprites.blinders import Blinder
from customSprites.smoke import Smoke
from customSprites.particle import Particle

# import fading_view as fv


class GameView(fading_view.FadingView):
    """Main Game Playing Screen class."""

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None
        self.carbinger_list = None
        self.blinder_list = None
        self.collision_text_list = []
        self.explosions_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.physics_engine = None
        self.scene = arcade.Scene()
        self.start_time = time()
        # Flag for game status
        self.is_game_over = False
        # Game over parameters
        self.game_over_text = "GAME OVER!"
        self.game_over_xpos = 0
        self.game_over_ypos = 0
        self.article_list = []

    def setup(self, *args, **kwargs):
        """Set up game board. Call this function to restart the game."""
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.carbinger_list = arcade.SpriteList(use_spatial_hash=True)
        self.blinder_list = arcade.SpriteList(use_spatial_hash=True)
        self.explosions_list = arcade.SpriteList()
        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = player.Player()
        self.player_list.append(self.player_sprite)
        # Set up list of articles for collisions
        self.article_list = config.saved_articles

        # Create the bounding box
        for x in range(0, SCREEN_WIDTH, 24):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.scene.add_sprite("Walls", wall)
            wall2 = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall2.center_x = x
            wall2.center_y = SCREEN_HEIGHT
            self.scene.add_sprite("Walls", wall2)

        for y in range(0, SCREEN_HEIGHT, 24):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.scene.add_sprite("Walls", wall)
            wall2 = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall2.center_y = y
            wall2.center_x = SCREEN_WIDTH
            self.scene.add_sprite("Walls", wall2)

        for i in range(STARTING_CAR_COUNT):
            new_carbinger = CarFactory.build_car()
            self.carbinger_list.append(new_carbinger)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.collision_text_draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.carbinger_list.draw()
        self.blinder_list.draw()
        self.explosions_list.draw()

    def collision_text_draw(self):
        """Display text on collision."""
        for txt in self.collision_text_list:
            display.display_collision_text(
                text=txt[0], xpos=txt[1], ypos=txt[2], fnt_sz=txt[3], clr=txt[4]
            )
            txt[3] -= txt[5]
            if txt[3] < 3:
                self.collision_text_list.remove(txt)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key in config.PLAYER_MOVE_KEYS:
            self.player_sprite.move_keydown(key)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key in config.PLAYER_MOVE_KEYS:
            self.player_sprite.move_keyup(key)

    def update_cars(self):
        """Logic for moving cars and expiring offscreen cars"""
        for car in self.carbinger_list:
            car.car_move()
            car.cooldown -= 1
            if car.center_x < 0 or car.center_x > SCREEN_WIDTH:
                car.remove_from_sprite_lists()
                if len(self.carbinger_list) < MAX_CAR_CT:
                    for i in range(CAR_SPAWN_RATE):
                        self.carbinger_list.append(CarFactory.build_car())

    def update_blinders(self):
        """Logic for moving cars and expiring offscreen cars"""
        for bl in self.blinder_list:
            bl.blinder_move()
            if (
                (bl.center_x < 0)
                or (bl.center_x > SCREEN_WIDTH)
                or (bl.center_y < 0)
                or (bl.center_y > SCREEN_HEIGHT)
            ):
                bl.remove_from_sprite_lists()

    def process_collisions(self):
        """Check for player collisions with other objects and act."""
        # Process Blinder collisions
        if self.blinder_list:
            blinder_hit_list = arcade.check_for_collision_with_list(
                self.player_sprite, self.blinder_list
            )
            for bl in blinder_hit_list:  # NewsFlash
                self.player_sprite.update_history(
                    bl, len(self.blinder_list), len(self.carbinger_list), txt="Excuses, Excuses"
                )
                self.player_sprite.blinder_count += 1
                bl.remove_from_sprite_lists()
                self.collision_text_list.append(
                    [
                        str(self.player_sprite.blinder_count),
                        bl.center_x,
                        bl.center_y,
                        BLINDER_HIT_TEXT_PERMANENCE,
                        BLINDER_HIT_TEXT_COLOR,
                        BLINDER_HIT_TEXT_DECAY_RATE,
                    ]
                )

        # Process_car_collisions
        car_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.carbinger_list)
        for nf in car_hit_list:  # NewsFlash
            if nf.cooldown < 0:
                article = replenish_articles(
                    threat=nf.objecttype, stored_articles=self.article_list
                )
                # removed\n{self.player_sprite.blinder_count}"
                collision_string = f"{nf.objecttype.upper().replace('_' , ' ')}\n{article.title()}"
                self.collision_text_list.append(
                    [
                        collision_string,
                        nf.center_x,
                        nf.center_y,
                        CAR_HIT_TEXT_PERMANENCE,
                        nf.color,
                        CAR_HIT_TEXT_DECAY_RATE,
                    ]
                )

                self.player_sprite.update_history(
                    nf, len(self.blinder_list), len(self.carbinger_list), txt=collision_string
                )
                nf.cooldown = 100
                self.player_sprite.blinder_count -= 1
                # Get an article related to the threat, or fetch new ones if no articles exist

                print(
                    f"Blinder count: {self.player_sprite.blinder_count},\n  collision string: {collision_string}"
                )
                self.car_explosion(nf)
                if self.player_sprite.blinder_count < 1:
                    self.end_game(nf)

    def car_explosion(self, nf):
        for i in range(PARTICLE_COUNT):
            particle = Particle(self.explosions_list)
            particle.position = nf.position
            self.explosions_list.append(particle)

        smoke = Smoke(50)
        smoke.position = nf.position
        self.explosions_list.append(smoke)

    def end_game(self, nf=arcade.Sprite):
        """Set game over message to display at the (x,y) position of the collision."""
        self.game_over_xpos = nf.center_x
        self.game_over_ypos = nf.center_y
        # Set game over flag so we can draw the game over message and stop the game
        self.is_game_over = True

    def spawn_blinders(self):
        """Create new blinders."""
        if uniform(0, 1) < BLINDER_SPAWN_RATE:
            bl = Blinder()
            self.blinder_list.append(bl)

    def on_update(self, delta_time):
        """Movement and game logic."""
        # Move the player with the physics engine
        self.physics_engine.update()
        self.update_cars()
        self.player_sprite.update_animation()
        self.update_blinders()
        self.process_collisions()
        self.explosions_list.update()
        # If game is over, switch to the game over view
        self.spawn_blinders()
        if self.is_game_over:
            # Take a snapshot of the game state so we can overlay the game over text on top
            game_over_texture = arcade.Texture("game over screenshot", get_image())
            config.df_collision_history.to_csv(RESOURCE_DIR / "collision history.csv")
            # Create new game over view using the saved game over parameters
            view = GameOverView(
                text=self.game_over_text,
                xpos=self.game_over_xpos,
                ypos=self.game_over_ypos,
                txtr=game_over_texture,
            )
            # Display the game over view
            self.window.show_view(view)


def main():
    """Launch the game."""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
