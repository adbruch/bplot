from bplot.check_data import check_data
from bplot.line import line_h, line_v
from bplot.point import point
import numpy as np


def percentile(
    x,
    y,
    outer=0.8,
    inner=0.5,
    color="tab:blue",
    label="",
    style="o",
    alpha=1.0,
    ax=None,
    **kws
):
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

    style : string, 'o' by default
        The shape of the median within the box.

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

    _, y, ax = check_data(None, y, ax)

    alpha_l, alpha_lm = (1 - outer) / 2, (1 - inner) / 2
    l, lm, m, um, u = alpha_l, alpha_lm, 0.5, 1 - alpha_lm, 1 - alpha_l
    q_l, q_lm, q_m, q_um, q_u = np.percentile(y, np.array([l, lm, m, um, u]) * 100)

    line_v(x, q_l, q_u, size=2, color=color, alpha=alpha)
    line_v(x, q_lm, q_um, size=5, color=color, alpha=alpha)

    out = point(x, q_m, size=2, style=style, color=color, label=label, alpha=alpha)
    return out


def percentile_h(
    x,
    y,
    outer=0.8,
    inner=0.5,
    color="tab:blue",
    label="",
    style="o",
    alpha=1,
    ax=None,
    **kws
):
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

    style : string, 'o' by default
        The shape of the median within the box.

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

    alpha_l, alpha_lm = (1 - outer) / 2, (1 - inner) / 2
    l, lm, m, um, u = alpha_l, alpha_lm, 0.5, 1 - alpha_lm, 1 - alpha_l
    q_l, q_lm, q_m, q_um, q_u = np.percentile(x, np.array([l, lm, m, um, u]) * 100)

    line_h(y, q_l, q_u, size=2, color=color, alpha=alpha)
    line_h(y, q_lm, q_um, size=5, color=color, alpha=alpha)

    out = point(q_m, y, size=2, style=style, color=color, label=label, alpha=alpha)
    return out
