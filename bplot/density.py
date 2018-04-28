from .check_data import check_data
import numpy as np
from scipy import stats

all = ['density']


def density(x,
            color='tab:blue',
            label='',
            bw_method=None,
            n=101,
            ax=None,
            **kws):
    """Draw density plot.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of data for which the standard five number summary
        is sought.

    color : string, 'tab:blue' by default
        The color of the line of the density plot.

    label : string, '' (empty) by default
        The label within a potential legend.

    bw_method : string, None by default
        TODO (ear) The bandwidth method used for smoothing.

    n : int, 101 by default
        The number of interpolatino points.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, _, ax = check_data(x, None, ax)

    (x_min, x_max) = np.min(x), np.max(x)
    xs = np.linspace(x_min, x_max, n)

    density = stats.kde.gaussian_kde(x, bw_method)
    out = ax.plot(xs, density(xs), color=color, label=label, **kws)
    return out
