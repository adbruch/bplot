from bplot.check_data import check_data
from bplot.line import line
import numpy as np


def trace(
    x, color="tab:blue", label="", style="-", size=1.5, alpha=1.0, ax=None, **kws
):
    """Draw trace plot.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the density is sought.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, '-' by default
        The line style of the curve.

    size : float, 1.5 by default
        The line width of the curve.

    alpha : float, 1.0 by default
        The transparency of the color.  Values between 0 (transparent) and 1 (opague) are allowed.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    out = line(
        np.arange(len(x)),
        x,
        color=color,
        label=label,
        style=style,
        size=size,
        alpha=alpha,
        **kws
    )
    return out
