# ------------------------------------------------------
# ------------- MatplotLib Dependencies ----------------
# ------------------------------------------------------
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")

class mplcanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.fog=fig
        self.axes = fig.add_subplot(1,1,1)
        super().__init__(fig)