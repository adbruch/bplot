from bplot.check_data import check_data
import matplotlib.pyplot as plt


def rug(x, y=0, color="tab:blue", label="", alpha=1, ax=None, **kws):
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

    out = ax.plot(
        x, [y] * len(x), marker="|", linestyle="", c=color, alpha=alpha, **kws
    )
    return out
