from bplot.check_data import check_data


def curve(
    x, y, color="tab:blue", label="", style="-", size=1.5, alpha=1, ax=None, **kws
):
    """Draw curve.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points for which the curve is drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points for which the curve is drawn.

    color : string, 'tab:blue' by default
        The color of the curve.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, '-' by default
        The line style of the curve.

    size : float, 1.5 by default
        The line width of the curve.

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

    x, y, ax = check_data(x, y, ax)

    out = ax.plot(
        x,
        y,
        color=color,
        label=label,
        linestyle=style,
        linewidth=size,
        alpha=alpha,
        **kws
    )
    return out
