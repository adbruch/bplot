import numpy as np
from bplot.check_data import check_data
from bplot.line import line_h, line_v
from bplot.point import point


def _bx(x):
    """Compute five numbers for box plot."""
    q1, q2, q3 = np.percentile(x, [25, 50, 75])
    iqr = q3 - q1

    x_min = x.min()
    x_max = x.max()

    uw = q3 + iqr * 1.5
    uw = np.clip(uw, q3, x_max)

    lw = q1 - iqr * 1.5
    lw = np.clip(lw, x_min, q1)

    return q1, q2, q3, lw, uw


def box(x, y, color="tab:blue", label="", style="o", alpha=1.0, ax=None, **kws):
    """Draw vertical box plot.

    Parameters
    ----------
    x : scalar
        The location along the x-axis at which the vertical box is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard five number summary
        is sought.

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

    q1, q2, q3, lw, uw = _bx(y)

    line_v(x, lw, uw, size=2, color=color, alpha=alpha)
    line_v(x, q1, q3, size=5, color=color, alpha=alpha)

    u_outs = y[np.where(y > uw)]
    l_outs = y[np.where(y < lw)]

    point(np.repeat(x, u_outs.size), u_outs, style="*", color=color, alpha=alpha)
    point(np.repeat(x, l_outs.size), l_outs, style="*", color=color, alpha=alpha)

    out = point(x, q2, color=color, label=label, size=2, style=style, alpha=alpha)
    return out


def box_h(x, y, color="tab:blue", label="", style="o", alpha=1.0, ax=None, **kws):
    """Draw horizontal box plot.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard five number summary
        is sought.

    y : scalar
        The location along the x-axis at which the vertical box is placed.

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

    q1, q2, q3, lw, uw = _bx(x)

    line_h(y, lw, uw, size=2, color=color, alpha=alpha)
    line_h(y, q1, q3, size=5, color=color, alpha=alpha)

    u_outs = x[np.where(x > uw)]
    l_outs = x[np.where(x < lw)]

    point(u_outs, np.repeat(y, u_outs.size), style="*", color=color, alpha=alpha)
    point(l_outs, np.repeat(y, l_outs.size), style="*", color=color, alpha=alpha)

    out = point(q2, y, size=2, style=style, color=color, label=label, alpha=alpha)
    return out
