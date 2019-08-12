from bplot.check_data import check_data


def line(
    x, y, color="tab:blue", label="", style="-", size=1.5, alpha=1, ax=None, **kws
):
    """Draw line.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points for the line is drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points for the curve is drawn.

    color : string, 'tab:blue' by default
        The color of the box.

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


def line_h(
    y,
    xmin=0,
    xmax=1,
    color="tab:blue",
    label="",
    style="-",
    size=1.5,
    alpha=1,
    ax=None,
    **kws
):
    """Draw horizontal line at y.


    Parameters
    ----------
    y : scalar
        The value on the y-axis for which the horizontal line is drawn.

    xmin : scalar, 0 by default
        The value on the x-axis for which the line starts.

    xmax : scalar, 1 by default
            The value on the x-axis for which the line ends.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, '-' by default
        The line style of the curve.

    size : float, 1.5 by default
        The line width of the curve.

    alpha : float, 1.0 by default
        The transparency of the color.
        Values between 0 (transparent) and 1 (opague) are allowed.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.

   """
    _, _, ax = check_data(None, None, ax)

    out = ax.axhline(
        y,
        xmin,
        xmax,
        color=color,
        label=label,
        linestyle=style,
        linewidth=size,
        alpha=alpha,
        **kws
    )
    return out


def line_v(
    x,
    ymin=0,
    ymax=1,
    color="tab:blue",
    label="",
    style="-",
    size=1.5,
    alpha=1,
    ax=None,
    **kws
):
    """Draw vertical line at x.

    Parameters
    ----------
    x : scalar
        The value on the x-axis for which the vertical line is drawn.

    ymin : scalar, 0 by default
        The value on the y-axis for which the line starts.

    ymax : scalar, 1 by default
            The value on the y-axis for which the line ends.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, '-' by default
        The line style of the curve.

    size : float, 1.5 by default
        The line width of the curve.

    alpha : float, 1.0 by default
        The transparency of the color.
        Values between 0 (transparent) and 1 (opague) are allowed.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.

   """
    _, _, ax = check_data(None, None, ax)

    out = ax.axvline(
        x,
        ymin,
        ymax,
        color=color,
        label=label,
        linestyle=style,
        linewidth=size,
        alpha=alpha,
        **kws
    )
    return out
