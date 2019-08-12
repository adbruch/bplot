from bplot.check_data import check_data
import matplotlib.pyplot as plt
import numpy as np


def jitter(
    x,
    y,
    jitter_x=0.4,
    jitter_y=0.4,
    color="tab:blue",
    label="",
    style="o",
    size=36,
    alpha=1,
    ax=None,
    **kws
):
    """Draw jittered points.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which jittered points are drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which jittered points are drawn.

    jitter_x : float, 0.4 by default
        The resolution of the jitter for the x-axis values.

    jitter_y : float, 0.4 by default
        The resolution of the jitter for the y-axis values.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, 'o' by default
        The shape of the points to draw.

    size : int, 36 by default
        The size of the points to draw.

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

    x, y, ax = check_data(x, y, ax)

    # TODO add user controlled resolution
    resolution_x = np.min(np.diff(np.sort(np.unique(x))).tolist() or 1)
    resolution_y = np.min(np.diff(np.sort(np.unique(x))).tolist() or 1)

    r_x = resolution_x / 2
    r_y = resolution_y / 2

    jx = jitter_x * np.random.uniform(low=-r_x, high=r_x, size=x.shape[0])
    jy = jitter_y * np.random.uniform(low=-r_y, high=r_y, size=y.shape[0])

    out = ax.scatter(
        x + jx, y + jy, c=color, label=label, marker=style, s=size, alpha=alpha, **kws
    )
    return out
