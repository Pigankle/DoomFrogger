from pathlib import Path
from dataclasses import dataclass
from configuration.color_table import COLORS

"""WINDOW PARAMETERS"""
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Doom Frogger"
TILE_SCALING = 0.1
SPLASH_IMAGE = "images/DoomFroggerLogo.png"
"""Text display"""
FONT_SIZE = 16
FONT_COLOR = (255, 255, 255)
TEXT_WIDTH = 200
GAME_OVER_IMAGE_PATH = "images/game_over.png"
RESOURCE_DIR = Path(__file__).parent.parent
HISTORY_FILE = "../collision history.csv"
""" PLAYER BEHAVIOR"""

PLAYER_MOVEMENT_SPEED = 5
PLAYER_SPRITE_IMG = "images/FrogSprite.png"
PLAYER_STARTING_POSITION = {"x": 300, "y": 20}
PLAYER_TEXTURE = "images/FrogSprite.png"
PLAYER_CHARACTER_SCALING = 0.1
UPDATES_PER_FRAME = 5

"""BLINDER BEHAVIOR """
BLINDER_DEFAULT_ICON = "images/rose.png"
BLINDER_SCALE = 0.1
BLINDER_SPAWN_RATE = 0.01
BLINDER_HIT_TEXT_COLOR = COLORS["PINK"]
BLINDER_HIT_FONT = "comic"
BLINDER_HIT_TEXT_PERMANENCE = 15
BLINDER_HIT_TEXT_DECAY_RATE = 0.1
BLINDER_CT_START = 1

"""CARBINGER PARAMETERS"""
STARTING_CAR_COUNT = 1
CAR_SCALE = 0.05
CAR_DEFAULT_ICON = "images/carbinger-light.png"
CAR_SPAWN_RATE = 2
MAX_CAR_CT = 50
CAR_HIT_TEXT_PERMANENCE = 15
CAR_HIT_TEXT_DECAY_RATE = 0.2


@dataclass
class CarSpec:
    objecttype: str = "climate_change"
    color: (int, int, int) = COLORS["RED"]
    speed: float = 6
    icon: str = "images/carbinger-light.png"


"""THREATS:
 Icons should be facing to the left if they have left-right orientation
 Horseman icon source: https://www.pngegg.com/en/png-cevbs
"""
CAR_TYPES = [
    CarSpec("climate_change", COLORS["RED"], 6, CAR_DEFAULT_ICON),
    CarSpec("famine", COLORS["BLACK"], 1, CAR_DEFAULT_ICON),
    CarSpec("nuclear_war", COLORS["ORANGE"], 5, CAR_DEFAULT_ICON),
    CarSpec("pandemic", COLORS["CHARTREUSE"], 4, CAR_DEFAULT_ICON),
    CarSpec("machine_superintelligence", COLORS["INDIGO"], 3, CAR_DEFAULT_ICON),
    CarSpec("crop_failure", COLORS["BROWN"], 2, CAR_DEFAULT_ICON),
]

""" --- Explosion Particles Related"""

# How fast the particle will accelerate down. Make 0 if not desired
PARTICLE_GRAVITY = 0.05
# How fast to fade the particle
PARTICLE_FADE_RATE = 8
# How fast the particle moves. Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5
# How many particles per explosion
PARTICLE_COUNT = 20
# How big the particle
PARTICLE_RADIUS = 3
# Possible particle colors
PARTICLE_COLORS = [
    COLORS["CRIMSON"],
    COLORS["COQUELICOT"],
    COLORS["LAVA"],
    COLORS["KU_CRIMSON"],
    COLORS["DARK_TANGERINE"],
]
# Chance we'll flip the texture to white and make it 'sparkle'
PARTICLE_SPARKLE_CHANCE = 0.02
# --- Smoke
# Note: Adding smoke trails makes for a lot of sprites and can slow things
# down. If you want a lot, it will be necessary to move processing to GPU
# using transform feedback. If to slow, just get rid of smoke.
# Start scale of smoke, and how fast is scales up
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03
# Rate smoke fades, and rises
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5
# Chance we leave smoke trail
SMOKE_CHANCE = 0.25

"""ARTICLE SEARCH PARAMETERS"""
NUM_ARTICLES = 5

# Define news website URLs
SEARCH_URL = "https://apnews.com/hub"
OUTPUT_URL = "https://apnews.com"

# Keywords for themes
KEYWORDS = {
    "climate_change": {
        "path": "/climate-change",
        "keywords": ["environment", "greenhouse", "climate"],
    },
    "famine": {
        "path": "/famine",
        "keywords": ["famine", "hunger", "starve", "starving", "shortage"],
    },
    "nuclear_war": {
        "path": "/nuclear-weapons",
        "keywords": ["nuclear", "radioactive", "russia", "ukraine", "north korea"],
    },
    "pandemic": {
        "path": "/health",
        "keywords": ["covid", "pandemic", "flu", "pox", "infection"],
    },
    "machine_superintelligence": {
        "path": "/artificial-intelligence",
        "keywords": ["artificial-inte", "artificial intelligence", "robot", "superintelligen"],
    },
    "crop_failure": {
        "path": "/agriculture",
        "keywords": [
            "failure",
            "drought",
            "flood",
            "struggle",
            "pest",
            "locust",
            "shortage",
            "flu",
            "disease",
            "rot",
            "blight",
        ],
    },
}
