from .check_data import check_data

def violin(x, y, color='tab:blue', label='', bw_method=None, n=101, ax=None, **kws):
    """Draw vertical violin plot.

    Parameters
    ----------
    x : int
        The location along the x-axis at which the vertical violin is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the violin plot is sought.

    color : string, 'tab:blue' by default
        The color of the line of the violin plot.

    label : string, '' (empty) by default
        The label within a potential legend.

    bw_method : string, None by default
        The bandwidth estimator method.  If None, 'scott' is used.

    n : int, 101 by default
        The number of interpolation points.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    ax : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    _, y, ax = check_data(None, y, ax)

    parts = ax.violinplot(y, positions=[x], bw_method=bw_method,
                          showmeans=False, showextrema=False, showmedians=False, points=n)

    if color:
        parts['bodies'][0].set_facecolor(color)

    return ax


def violin_h(x, y, color='tabl:blue', label='', bw_method=None, n=101, ax=None, **kws):
    """Draw horizontal violin plot.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the violin plot is sought.

    y : int
        The location along the y-axis at which the horizontal violin is placed.

    color : string, 'tab:blue' by default
        The color of the line of the violin plot.

    label : string, '' (empty) by default
        The label within a potential legend.

    bw_method : string, None by default
        The bandwidth estimator method.  If None, 'scott' is used.

    n : int, 101 by default
        The number of interpolation points.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    ax : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    parts = ax.violinplot(x, positions=[y], bw_method=bw_method, vert=False,
                          showmeans=False, showextrema=False, showmedians=False, points=n)

    if color:
        parts['bodies'][0].set_facecolor(color)

    return ax
