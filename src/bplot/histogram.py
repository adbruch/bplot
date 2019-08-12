from bplot.check_data import check_data
from bplot.bayesian_blocks import bayesian_blocks


def histogram(
    x,
    color="tab:blue",
    label="",
    style="-",
    size=1.5,
    alpha=1,
    bins="auto",
    ax=None,
    **kws
):
    """Draw a histogrm.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data from which the histogram is drawn.

    color : string, 'tab:blue' by default
        The color of the outline of the histogram.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, '-' by default
        The line style of the curve.

    size : float, 1.5 by default
        The line width of the curve.

    alpha : float, 1.0 by default
        The transparency of the color.  Values between 0 (transparent) and 1 (opague) are allowed.

    bins : {int, string}, 'auto' by default
        The number of bins.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------
    (n, bins, patches) : 3-tuple
        `n` is ... TODO (ear) copy output from matplotlib
        `bins` ...
        `patches` ...
    """

    x, _, ax = check_data(x, None, ax)

    if bins == "bayesian_blocks" or bins == "bb":
        bins = bayesian_blocks(x)

    n, bins, patches = ax.hist(
        x,
        color=color,
        label=label,
        linestyle=style,
        linewidth=size,
        alpha=alpha,
        density=True,
        histtype="step",
        bins=bins,
    )
