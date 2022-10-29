import player
from car_factory import CarFactory
from constants import *

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

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.physics_engine = None
        self.scene = arcade.Scene()

    def setup(self):
        """Set up game board. Call this function to restart the game."""
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.carbinger_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = player.Player()
        self.player_list.append(self.player_sprite)

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

    def process_collisions(self):
        """What happens when cars and player collide"""
        hitlist = arcade.check_for_collision_with_list(self.player_sprite, self.carbinger_list)
        for nf in hitlist: #NewsFlash
            if nf.cooldown < 0:
                self.jiggle_player() #TODO Move this to player class
                self.display_news(threat = nf.threat,
                                  xpos = str(int(nf.center_x)),
                                  ypos = str(int(nf.center_y)))
                nf.cooldown = 100


    def display_news(self,threat, xpos, ypos ):
        #TODO don't use arcade.draw_text   Use an arcade.Text object
        #This function should probably be in the display.py class
        print(f"{threat} Detected at ({xpos}, {ypos})")

    def jiggle_player(self):#TODO Add animation to strike.  This should be in player class
        """jiggle the player for an animation effect"""
        pass

    def on_update(self, delta_time):
        """Movement and game logic"""
        # Move the player with the physics engine
        self.physics_engine.update()
        self.update_cars()
        self.process_collisions()

def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()