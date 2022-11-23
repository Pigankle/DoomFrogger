import pandas as pd
import arcade

# Mutable global variables

saved_articles = []
df_collision_history = pd.DataFrame()
PLAYER_MOVE_KEYS = [arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT]
