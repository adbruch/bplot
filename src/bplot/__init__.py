from bplot.show import show
from bplot.autocorrelation import autocorrelation
from bplot.box import box, box_h
from bplot.colors import color, tab_color, old_color, CatColors
from bplot.curve import curve
from bplot.density import density
from bplot.grid import grid
from bplot.histogram import histogram
from bplot.jitter import jitter
from bplot.lag import lag
from bplot.line import line, line_h, line_v
from bplot.lv import lv
from bplot.point import point
from bplot.scatter import scatter
from bplot.percentile import percentile, percentile_h
from bplot.rug import rug
from bplot.shade import shade_x, shade_y
from bplot.std import std, std_h
from bplot.ste import ste, ste_h
from bplot.mad import mad, mad_h
from bplot.trace import trace
from bplot.utilities import (
    clear,
    current_axis,
    hide_xaxis,
    hide_yaxis,
    labels,
    LaTeX,
    legend,
    save,
    subplots,
    title,
    xticks,
    yticks,
    tight_layout,
)
from bplot.violin import violin, violin_h

__version__ = "0.2"
