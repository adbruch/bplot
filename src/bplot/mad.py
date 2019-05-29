from bplot.check_data import check_data
import numpy as np
from scipy.stats import norm


def mad_std(x):
    return np.median(np.abs(x - np.median(x)))


def mad(x, y, z=1.96, z_inner=0.675, color="tab:blue", label="", shape="o", ax=None):
    """Draw vertical median absolute deviation intervals.


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

    _, y, ax = check_data(None, y, ax)

    med, mad = np.median(y), mad_std(y) / norm.ppf(0.75)

    lw_mid, uw_mid = med - z_inner * mad, med + z_inner * mad
    lw, uw = med - z * mad, med + z * mad

    ax.vlines(x, lw, uw, color=color)
    ax.vlines(x, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(x, med, markersize=10, marker=shape, color=color, label=label)
    return out


def mad_h(x, y, z=1.96, z_inner=0.675, color="tab:blue", label="", shape="o", ax=None):
    """Draw horizontal median absolute deviation intervals.


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

    x, _, ax = check_data(x, None, ax)

    med, mad = np.median(x), mad_std(x) / norm.ppf(0.75)

    lw_mid, uw_mid = med - z_inner * mad, med + z_inner * mad
    lw, uw = med - z * mad, med + z * mad

    ax.hlines(y, lw, uw, color=color)
    ax.hlines(y, lw_mid, uw_mid, lw=4, color=color)

    out = ax.plot(med, y, markersize=10, marker=shape, color=color, label=label)
    return out
