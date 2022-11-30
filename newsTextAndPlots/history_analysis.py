import io
import matplotlib.pyplot as plt
from PIL import Image
from configuration.constants import CAR_TYPES, SCREEN_HEIGHT, SCREEN_WIDTH
from configuration import config


class HistoryPlots:
    """Generate History Plots."""

    def __init__(self):
        self.colorlookup = {x.objecttype: self.hextriplet(x.color) for x in CAR_TYPES}
        self.colorlookup["Blinder"] = "#FFB6C1"

    def hextriplet(self, colortuple):
        """Convert RGB to hex values."""
        return "#" + "".join(f"{i:02X}" for i in colortuple)

    def make_threat_piechart(self, df):
        df_threats = df[df["HitType"] != "Blinder"]
        gb_threat = df_threats.groupby(["HitType"]).count()
        color_list = [self.colorlookup[threat] for threat in gb_threat.index]
        fig1, ax1 = plt.subplots()
        ax1.pie(gb_threat["PosY"], shadow=False, startangle=90, colors=color_list)
        lbl = [str.replace("_", " ").title() for str in gb_threat.index]
        ax1.axis("equal")
        plt.legend(loc="center", labels=lbl)
#        plt.show()
        return plt

        # %%

    def make_blinderct_timeline(self, df):
        print("\n\nMAKING TIMELINE\n\n")
        px = 0.01
        fig, ax = plt.subplots(figsize=(SCREEN_WIDTH * px * 0.8, SCREEN_HEIGHT * px * 0.1))
        ax.plot(df["Time"], df["PrevBlinderCount"], color="black")
        ax.scatter(
            df["Time"], df["PrevBlinderCount"], c=df["HitType"].map(self.colorlookup), zorder=3
        )
        return plt

    def get_plot_img(self, df=config.df_collision_history, plottype="pie"):
        if plottype == "pie":
            plt = self.make_threat_piechart(df)
        elif plottype == "line":
            plt = self.make_blinderct_timeline(df)
        else:
            pass
        retimg = self.fig2img(plt)
        return retimg

    def fig2img(self, fig):
        """Convert a Matplotlib figure to a PIL Image and return it."""
        buf = io.BytesIO()
        fig.savefig(buf, transparent=True)
        buf.seek(0)
        img = Image.open(buf)
        return img
