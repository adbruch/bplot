import numpy as np
from .check_data import check_data

all = ['percentile', 'percentile_h']

def percentile(x,
               y,
               outer=.8,
               inner=.5,
               color='tab:blue',
               label='',
               shape='o',
               ax=None,
               **kws):
    """Draw vertical percentile interval.


    Parameters
    ----------
    x : int
        The location along the x-axis at which the interval is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the `outer` percentile interval is sought.

    outer : float, 0.8 by default
        The outer interval percentage.

    inner : float, 0.5 by default
        The inner interval percentage.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    shape : string, 'o' by default
        The shape of the median within the box.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    _, y, ax = check_data(None, y, ax)

    alpha_l, alpha_lm = (1 - outer) / 2, (1 - inner) / 2
    l, lm, m, um, u = alpha_l, alpha_lm, .5, 1 - alpha_lm, 1 - alpha_l
    q_l, q_lm, q_m, q_um, q_u = np.percentile(y, np.array([l, lm, m, um, u]) * 100)

    ax.vlines(x, q_l, q_u, color=color)
    ax.vlines(x, q_lm, q_um, lw=4, color=color)

    out = ax.plot(x, q_m, markersize=10, marker=shape, color=color, label=label)
    return out


def percentile_h(x, y, outer=.8, inner=.5, color='tab:blue', label='', shape='o', ax=None, **kws):
    """Draw horizontal percentile interval.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the `outer` percentile interval is sought.

    y : int
        The location along the y-axis at which the interval is placed.

    outer : float, 0.8 by default
        The outer interval percentage.

    inner : float, 0.5 by default
        The inner interval percentage.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    shape : string, 'o' by default
        The shape of the median within the box.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    alpha_l, alpha_lm = (1 - outer) / 2, (1 - inner) / 2
    l, lm, m, um, u = alpha_l, alpha_lm, .5, 1 - alpha_lm, 1 - alpha_l
    q_l, q_lm, q_m, q_um, q_u = np.percentile(x, np.array([l, lm, m, um, u]) * 100)

    ax.hlines(y, q_l, q_u, color=color)
    ax.hlines(y, q_lm, q_um, lw=4, color=color)

    out = ax.plot(q_m, y, markersize=10, marker=shape, color=color, label=label)
    return out
