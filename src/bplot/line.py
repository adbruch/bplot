from bplot.check_data import check_data

all = ['line']

def line(x, y, color='tab:blue', alpha=1, label='', ax=None, **kws):
    """Draw line.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis points for the line is drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis points for the curve is drawn.

    color : string, 'tab:blue' by default
        The color of the box.

    alpha : float, 1.0 by default
        The transparency of the color.  Values between 0 (transparent) and 1 (opague) are allowed.

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

    x, y, ax = check_data(x, y, ax)

    out = ax.plot(x, y, '-', color=color, alpha=alpha, label=label, **kws)
    return out
