from bplot.check_data import check_data
from bplot.point import point


def lag(
    x, lag=1, color="tab:blue", label="", style="o", size=1.0, alpha=1.0, ax=None, **kws
):
    """Draw lag plot.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The location along the x-axis at which the lags are drawn.

    lag : float, 1 by default
        The lag of the plot.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    size : int, 1 by default
        The size of the points to draw.  In matplotlib terms, this is equivalent to mpl.rcParam['lines.markersize'] = 6**(size + 1).

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

    y1 = x[:-lag]
    y2 = x[lag:]

    out = point(
        y1,
        y2,
        color=color,
        label=label,
        style=style,
        size=size,
        alpha=alpha,
        ax=ax,
        **kws
    )
    return out
