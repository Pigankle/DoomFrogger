import arcade as arc
import random
from configuration import config
import views.fading_view as fv
import views.splash_view as sv
from configuration.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE
from newsTextAndPlots import display
from newsTextAndPlots.history_analysis import HistoryPlots


# View for when the game is over
class GameOverView(fv.FadingView):
    """Create view to show when game is over."""

    def __init__(self, *args, **kwargs):
        """Create view."""
        super().__init__()
        self.texture = kwargs["txtr"]
        self.game_over_text = kwargs["text"]
        self.game_over_xpos = kwargs["xpos"]
        self.game_over_ypos = kwargs["ypos"]
        self.df_result = config.df_collision_history
        self.admonishment = arc.Text(
            f"You ignored {(~self.df_result['HitType'].str.contains('Blinder')).sum()}"
            f" warnings.  Why won't you listen?\n\n"
            f"Click to try again, press 'q' to exit.",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arc.color.RED,
            30,
            anchor_x="center",
            multiline=True,
            width=SCREEN_WIDTH * 0.8,
        )
        self.active_warning = None
        self.warning_list = []
        self.warning_growing = True

        arc.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        hcht = HistoryPlots()
        self.hist_plot_line = hcht.get_plot_img(df=self.df_result, plottype="line")
        self.hist_plot_pie = hcht.get_plot_img(df=self.df_result, plottype="pie")
        print(f"{self.hist_plot_line=}")
        self.setup()

    def setup(self):
        """Set up class."""
        self.warning_list = arc.SpriteList()

        df_threats = self.df_result[self.df_result["HitType"] != "Blinder"]
        for index, row in df_threats.iterrows():
            print(row["Color"])
            newsprite = arc.create_text_sprite(
                text=row["Text"],
                start_x=row["PosX"],
                start_y=row["PosY"],
                font_size=FONT_SIZE,
                color=row["Color"],
            )
            newsprite.scale = 0.1
            self.warning_list.append(newsprite)
        self.active_warning = self.warning_list[0]
        print(self.active_warning)
        self.warning_growing = True

    def on_update(self, dt):
        """Process updates."""
        self.update_fade(next_view=sv.SplashView)
        self.update_warning_text()

    def on_draw(self):
        """Draw this view."""
        self.clear()
        self.texture.draw_sized(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 150
        )
        display.display_headline_text(
            text=self.game_over_text, xpos=self.game_over_xpos, ypos=self.game_over_ypos
        )
        self.draw_plots()
        self.admonishment.draw()
        self.update_warning_text()
        self.active_warning.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If the user presses the mouse button, re-start the game."""
        self.next_view = sv.SplashView
        if self.fade_out is None:
            self.fade_out = 0

    def on_key_press(self, key, _modifiers):
        """Go back to the main menu view when user hits q."""
        if key == arc.key.Q:
            arc.exit()

    def draw_plots(self):
        """Create plots for recap."""
        pie_texture = arc.Texture("Pie Chart", self.hist_plot_pie)
        line_texture = arc.Texture("Time Line", self.hist_plot_line)
        arc.draw_scaled_texture_rectangle(
            center_x=175, center_y=SCREEN_HEIGHT - 175, texture=pie_texture, scale=1, alpha=200
        )
        # TODO add plot labels
        arc.draw_scaled_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 8,
            texture=line_texture,
            scale=1.5,
            alpha=200,
        )

    def update_warning_text(self):
        """Grow and Shrink recap text."""
        if self.warning_growing:
            self.active_warning.scale += 0.005
            if self.active_warning.scale > 1.1:
                self.warning_growing = False
        else:
            self.active_warning.scale -= 0.005
            if self.active_warning.scale < 0.1:
                self.warning_growing = True
                self.active_warning = random.choice(self.warning_list)
