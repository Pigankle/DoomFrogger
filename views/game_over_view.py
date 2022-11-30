import arcade as arc
import random
from configuration import config
import views.fading_view as fv
import views.splash_view as sv
from configuration.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE, ADMONISHMENTS_LIST
from newsTextAndPlots.history_analysis import HistoryPlots
from customSprites.carbinger import Carbinger


# View for when the game is over
class GameOverView(fv.FadingView):
    """Create view to show when game is over."""

    def __init__(self, *args, **kwargs):
        """Create view."""
        super().__init__()

    def setup(self):
        self.df_result = config.df_collision_history
        print(f"{self.df_result.info()=}")
        self.admonishment = arc.Text(
            f"Things didn't work out so well for you.",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arc.color.RED,
            30,
            anchor_x="center",
            multiline=True,
            width=SCREEN_WIDTH * 0.8,
        )
        self.active_warning = None
        self.warning_growing = True
#        self.hist_plot_line = None
 #       self.hist_plot_pie = None
#        self.line_texture = None
#        self.pie_texture = None
        arc.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.car_list = arc.SpriteList()
        self.warning_list = arc.SpriteList()

        df_threats = self.df_result[self.df_result["HitType"] != "Blinder"]
        for index, row in df_threats.iterrows():
            print(f"A text sprite at {row['PosX']=}")
            history_text_sprite = arc.create_text_sprite(
                text=row["Text"],
                start_x=row["PosX"],
                start_y=row["PosY"],
                font_size=FONT_SIZE,
                color=row["Color"],
            )
            history_text_sprite.scale = 0.1
            self.warning_list.append(history_text_sprite)

        # Control Variables
        self.plot_alpha_incr = 200 / len(df_threats)  # To control the fadein of the plots
        self.plot_alpha = 10
        self.create_plots()
        self.threat_iter = -1  # to Aid iterating through threat list
        self.warning_growing = True
        self.next_warning()


    def create_plots(self):
        hcht = HistoryPlots()
        self.hist_plot_line = hcht.get_plot_img(df=self.df_result, plottype="line")
        self.hist_plot_pie = hcht.get_plot_img(df=self.df_result, plottype="pie")
        self.line_texture = arc.Texture("Time Line", self.hist_plot_line)
        self.pie_texture = arc.Texture("Pie Chart", self.hist_plot_pie)

    def on_update(self, dt):
        """Process updates."""
        self.update_fade(next_view=sv.SplashView)
        self.update_warning_text()

    def on_draw(self):
        """Draw this view."""
        self.clear()
        self.draw_plots()
        self.admonishment.draw()
        self.update_warning_text()
        self.active_warning.draw()
        self.car_list.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If the user presses the mouse button, re-start the game."""
        self.reset_stats()
        self.next_view = sv.SplashView
        if self.fade_out is None:
            self.fade_out = 0

    def on_key_press(self, key, _modifiers):
        """Quit when user hits q."""
        if key == arc.key.Q:
            arc.exit()

    def draw_plots(self):
        """Create plots for recap."""
        if self.pie_texture and self.line_texture:
            arc.draw_scaled_texture_rectangle(
                center_x=175,
                center_y=SCREEN_HEIGHT - 175,
                texture=self.pie_texture,
                scale=1,
                alpha=self.plot_alpha,
            )

            arc.draw_scaled_texture_rectangle(
                center_x=SCREEN_WIDTH / 2,
                center_y=SCREEN_HEIGHT / 8,
                texture=self.line_texture,
                scale=1.5,
                alpha=self.plot_alpha,
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
                self.next_warning()

    def next_warning(self):
        """Create the next warning text sprite and set behavior controls."""
        self.warning_growing = True
        self.plot_alpha = min(200, self.plot_alpha + self.plot_alpha_incr)

        self.threat_iter = min(self.threat_iter + 1, len(self.warning_list) - 1)
        self.active_warning = self.warning_list[self.threat_iter]
        if len(self.car_list) <= len(self.warning_list):
            self.car_list.append(
                self.create_history_car(
                    self.active_warning.center_x,
                    self.active_warning.center_y,
                    self.active_warning.color,
                )
            )
            self.admonishment = arc.Text(
                random.choice(ADMONISHMENTS_LIST)+" \n\n"
                "Click to try again, press 'q' to exit.",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                arc.color.RED,
                30,
                anchor_x="center",
                multiline=True,
                width=SCREEN_WIDTH * 0.8,
            )
        else:
            self.admonishment = arc.Text(
                f"You ignored {len(self.car_list)-1}"
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
            self.active_warning = random.choice(self.warning_list)

    def create_history_car(self, center_x, center_y, color):
        """Create car based on active_warning."""
        history_car = Carbinger()
        history_car.color = color
        history_car.center_x = center_x
        history_car.center_y = center_y
        return history_car

    def reset_stats(self):
        # TODO This shouldn't be necessary.  I am trying to get the plots to
        #  rerender on second game.  This doesn't do it.
        self.hist_plot_line = None
        self.hist_plot_pie = None
        self.line_texture = None
        self.pie_texture = None
