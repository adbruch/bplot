from bplot.check_data import check_data


def shade_x(
    x, y1, y2, where=None, color="tab:blue", label="", alpha=1.0, ax=None, **kws
):
    """Shade over x-axis.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points across which the shade will be drawn.

    y1 : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points which define the bottom of the shade.

    y2 : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points which define the top of the shade.

    where : array of bool, None by default
        Shaded regions are specified by True values.

    color : string, 'tab:blue' by default
        The color of the box.

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
    # TODO (ear): validate y1 and y2

    out = ax.fill_between(
        x, y1, y2, color=color, alpha=alpha, label=label, where=where, **kws
    )
    return out


def shade_y(y, x1, x2, where=None, color="tab:blue", label="", alpha=1, ax=None, **kws):
    """Shade over y-axis.


    Parameters
    ----------
    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points across which the shade will be drawn.

    x1 : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points which define the left of the shade.

    x2 : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points which define the right of the shade.

    where : array of bool, None by default
        Shaded regions are specified by True values.

    color : string, 'tab:blue' by default
        The color of the box.

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

    _, y, ax = check_data(None, y, ax)
    # TODO (ear): validate x1 and x2

    out = ax.fill_betweenx(
        y, x1, x2, color=color, label=label, alpha=alpha, where=where, **kws
    )
    return out
