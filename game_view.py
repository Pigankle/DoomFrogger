import player
import pandas as pd
from random import uniform
from car_factory import CarFactory
from arcade import get_image
from get_news import get_article
from display import display_text
from game_over_view import GameOverView
from constants import *
from blinders import Blinder



class GameView(arcade.View):
    """
    Main Game Playing Screen class.
    """

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

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.physics_engine = None
        self.scene = arcade.Scene()

    def setup(self):
        """Set up game board. Call this function to restart the game."""
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.carbinger_list = arcade.SpriteList(use_spatial_hash=True)
        self.blinder_list = arcade.SpriteList(use_spatial_hash=True)
        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = player.Player()
        self.player_list.append(self.player_sprite)
        
        # Flag for game status
        self.is_game_over = False

        # Game over parameters
        self.game_over_text = ""
        self.game_over_xpos = 0
        self.game_over_ypos = 0

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
            new_carbinger = CarFactory.new_car()
            self.carbinger_list.append(new_carbinger)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls") )

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()
        self.carbinger_list.draw()
        self.blinder_list.draw()
        self.collision_text_draw()

    def collision_text_draw(self):
        for txt in self.collision_text_list[:-1]:
            perm = txt[3]
            display_text(
                    text=txt[0],
                    xpos=txt[1],
                    ypos=txt[2],
                    fnt_sz = txt[3]
                )
            txt[3] -= .05
            if txt[3]<1:
                self.collision_text_list.remove(txt)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key in PLAYER_MOVE_KEYS:
            self.player_sprite.move_keydown(key)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key in PLAYER_MOVE_KEYS:
            self.player_sprite.move_keyup(key)

    def update_cars(self):
        """Logic for moving cars and expiring offscreen cars"""
        for car in self.carbinger_list:
            car.car_move()
            car.cooldown -=1
            if car.center_x <0 or car.center_x > SCREEN_WIDTH:
                car.remove_from_sprite_lists()
                if len(self.carbinger_list) < MAX_CAR_CT:
                    for i in range(CAR_SPAWN_RATE):
                        self.carbinger_list.append(CarFactory.new_car())

    def update_blinders(self):
        """Logic for moving cars and expiring offscreen cars"""
        for bl in self.blinder_list:
            bl.blinder_move()
            if ( (bl.center_x < 0) or (bl.center_x > SCREEN_WIDTH)
                    or (bl.center_y <0) or (bl.center_y>SCREEN_HEIGHT)):
                bl.remove_from_sprite_lists()

    def process_collisions(self):
        """What happens when player collides with other objects"""
        # Process Blinder collisions
        if self.blinder_list:
            blinder_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.blinder_list)
            for bl in blinder_hit_list:  # NewsFlash
                self.player_sprite.blinder_count += 1
                bl.remove_from_sprite_lists()
        # Process_car_collisions
        car_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.carbinger_list)
        for nf in car_hit_list: #NewsFlash
            if nf.cooldown < 0:
                self.player_sprite.jiggle()
                nf.cooldown = 100
                self.player_sprite.isStunned = 1
                self.player_sprite.blinder_count -= 1
                self.collision_text_list.append(
                    [f"{nf.threat.upper()}\n{self.player_sprite.blinder_count}", nf.center_x, nf.center_y,
                     COLLISION_TEXT_PERMANENCE])
                print(f"Blinder count is {self.player_sprite.blinder_count}")
            if self.player_sprite.blinder_count < 1:
                # Search for related new article, and store article title and URL
                article = get_article(nf.threat)
                # Set game over message and set the message to display at the (x,y) position of the collision
                self.game_over_text = f'GAME OVER!\n{article["text"]}\n{article["url"][0:35]}[...]'
                self.game_over_xpos = nf.center_x
                self.game_over_ypos = nf.center_y
                print(self.game_over_text)
                # Set game over flag so we can draw the game over message and stop the game
                self.is_game_over = True


    def spawn_blinders(self):
        """Create new blinders"""
        if uniform(0,1) < BLINDER_SPAWN_RATE:
            bl = Blinder()
            self.blinder_list.append(bl)


    def on_update(self, delta_time):
        """Movement and game logic"""
        # Move the player with the physics engine
        self.physics_engine.update()
        self.update_cars()
        self.update_blinders()
        self.process_collisions()
        # If game is over, switch to the game over view
        self.spawn_blinders()
        if (self.is_game_over == True):
            # Take a snapshot of the game state so we can overlay the game over text on top
            image = get_image()
            image.save(RESOURCE_DIR/ GAME_OVER_IMAGE_PATH, "PNG")
            # Create new game over view using the saved game over parameters
            view = GameOverView(
                text=self.game_over_text,
                xpos=self.game_over_xpos,
                ypos=self.game_over_ypos
                )
            # Display the game over view
            self.window.show_view(view)

def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()