"""
Create a display object so we can format text output
use https://api.arcade.academy/en/development/api_docs/api/text.html?highlight=text

"""
from arcade import Text
from constants import *

# Function to display text output at specified position
def display_text(text, xpos, ypos):
    text_obj = Text(
        text=text,
        start_x=xpos,
        start_y=ypos,
        color=FONT_COLOR,
        font_size=FONT_SIZE, 
        width=TEXT_WIDTH,
        align='left', 
        font_name='arial', 
        bold=True,
        multiline=True
        )
    text_obj.draw()
