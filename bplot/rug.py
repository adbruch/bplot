from .check_data import check_data
import matplotlib.pyplot as plt


def rug(x, y=0, color='tab:blue', label='', ax=None, **kws):
    """Draw rug.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis data for the rug is drawn.

    y : int, 0 by default
        The y-axis specifying the base of the rug.

    color : string, 'tab:blue' by default
        The color of the rug.

    label : string, '' (empty) by default
        The label within a potential legend.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    out = ax.plot(x, [y] * len(x), marker='|', linestyle='', c=color, **kws)
    return out
