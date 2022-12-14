"""
Create a display object so we can format text output.

use https://api.arcade.academy/en/development/api_docs/api/text.html?highlight=text
"""
from arcade import Text
from configuration.constants import FONT_SIZE, FONT_COLOR, TEXT_WIDTH


# Function to display text output at specified position
def display_headline_text(text, xpos, ypos, fnt_sz=FONT_SIZE):
    text_obj = Text(
        text=text,
        start_x=xpos,
        start_y=ypos,
        color=FONT_COLOR,
        width=TEXT_WIDTH,
        font_size=fnt_sz,
        align="left",
        font_name="arial",
        bold=True,
        multiline=True,
    )
    text_obj.draw()


def display_collision_text(text, xpos, ypos, fnt_sz, clr):
    text_obj = Text(
        text=text,
        start_x=xpos,
        start_y=ypos,
        color=clr,
        width=TEXT_WIDTH,
        font_size=fnt_sz,
        align="left",
        font_name="comic",
        bold=True,
        multiline=True,
    )
    text_obj.draw()
