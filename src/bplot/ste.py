from bplot.check_data import check_data
import numpy as np


def ste(x,
        y,
        z=1.96,
        z_inner=0.675,
        color='tab:blue',
        label='',
        shape='o',
        ax=None):
    """Draw vertical standard error intervals.


    Parameters
    ----------
    x : int
        The location along the x-axis at which the vertical interval is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard error is sought.

    z : float, 1.96 by default
        The number of standard deviations from the mean for the outer bound.

    z_inner : float, 0.675 by default
        The number of standard deviations from the mean for the inner bound.

    color : string, 'tab:blue' by default
        The color of the rug.

    label : string, '' (empty) by default
        The label within a potential legend.

    shape : string, 'o' by default
        The shape of the mean point.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    _, y, ax = check_data(None, y, ax)

    ybar, ste = np.mean(y), np.std(y) / np.sqrt(len(y))

    lw_mid, uw_mid = ybar - z_mid * ste, ybar + z_mid * ste
    lw, uw = ybar - z * ste, ybar + z * ste

    ax.vlines(x, lw, uw, color=color)
    ax.vlines(x, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(
        x, ybar, markersize=10, marker=shape, color=color, label=label)
    return out


def ste_h(x,
          y,
          z=1.96,
          z_mid=0.675,
          color='tab:blue',
          label='',
          shape='o',
          ax=None):
    """Draw horizontal standard error intervals.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard error is sought.

    y : int
        The location along the y-axis at which the vertical interval is placed.

    z : float, 1.96 by default
        The number of standard deviations from the mean for the outer bound.

    z_inner : float, 0.675 by default
        The number of standard deviations from the mean for the inner bound.

    color : string, 'tab:blue' by default
        The color of the rug.

    label : string, '' (empty) by default
        The label within a potential legend.

    shape : string, 'o' by default
        The shape of the mean point.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    xbar, ste = np.mean(x), np.std(x) / np.sqrt(len(x))

    lw_mid, uw_mid = xbar - z_mid * ste, xbar + z_mid * ste
    lw, uw = xbar - z * ste, xbar + z * ste

    ax.hlines(y, lw, uw, color=color)
    ax.hlines(y, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(
        xbar, y, markersize=10, marker=shape, color=color, label=label)
    return out
