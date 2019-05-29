import numpy as np
from bplot.check_data import check_data

all = ["box", "box_h"]


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


def box(x, y, color="tab:blue", label="", shape="o", ax=None, **kws):
    """Draw vertical box plot.

    Parameters
    ----------
    x : int
        The location along the x-axis at which the vertical box is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard five number summary
        is sought.

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

    q1, q2, q3, lw, uw = _bx(y)

    ax.vlines(x, lw, uw, color=color)
    ax.vlines(x, q1, q3, lw=4, color=color)
    # TODO(ear) add points outside of whiskers

    out = ax.plot(x, q2, markersize=10, marker=shape, color=color, label=label)
    return out


def box_h(x, y, color="tab:blue", label="", shape="o", ax=None, **kws):
    """Draw horizontal box plot.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard five number summary
        is sought.

    y : int
        The location along the x-axis at which the vertical box is placed.

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

    q1, q2, q3, lw, uw = _bx(x)

    ax.hlines(y, lw, uw, color=color)
    ax.hlines(y, q1, q3, lw=4, color=color)
    # TODO(ear) add points outside of whiskers

    out = ax.plot(q2, y, markersize=10, marker=shape, color=color, label=label)
    return out
