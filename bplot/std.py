from .check_data import check_data
import numpy as np


def std(x,
        y,
        z=1.96,
        z_inner=0.675,
        color='tab:blue',
        label='',
        shape='o',
        ax=None):
    """Draw vertical standard deviation intervals.


    Parameters
    ----------
    x : int
        The location along the x-axis at which the vertical interval is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard deviation is sought.

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

    x, y, ax = check_data(x, y, ax)

    ybar, std = np.mean(y), np.std(y)

    lw_mid, uw_mid = ybar - z_mid * std, ybar + z_mid * std
    lw, uw = ybar - z * std, ybar + z * std

    ax.vlines(x, lw, uw, color=color)
    ax.vlines(x, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(
        x, ybar, markersize=10, marker=shape, color=color, label=label)
    return out


def std_h(x,
          y,
          z=1.96,
          z_inner=0.675,
          color='tab:blue',
          label='',
          shape='o',
          ax=None):
    """Draw horizontal standard deviation intervals.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard deviation interval is sought.

    y : int
        The location along the y-axis at which the vertical interval is placed.

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

    if ax is None:
        ax = plt.gca()

    xbar, std = np.mean(x), np.std(x)

    lw_mid, uw_mid = xbar - z_mid * std, xbar + z_mid * std
    lw, uw = xbar - z * std, xbar + z * std

    ax.hlines(y, lw, uw, color=color)
    ax.hlines(y, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(
        xbar, y, markersize=10, marker=shape, color=color, label=label)
