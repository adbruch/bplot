from bplot.check_data import check_data
from bplot.bayesian_blocks import bayesian_blocks

all = ['histogram']


def histogram(x, color='tab:blue', label='', bins='auto',
              size=None, alpha=None, ax=None, layer=None):
    """Draw a histogrm.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data from which the histogram is drawn.

    color : string, 'tab:blue' by default
        The color of the outline of the histogram.

    label : string, '' (empty) by default
        The label within a potential legend.

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

    if bins == 'bayesian_blocks' or bins == 'bb':
        bins = bayesian_blocks(x)

    n, bins, patches = ax.hist(
        x, color=color, label=label, density=True, histtype='step',
        alpha=alpha, bins=bins, zorder=layer)
