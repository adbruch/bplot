from bplot.check_data import check_data
import numpy as np


all = ['autocorrelation']


def _autocorrelation(x):
    # https://lingpipe-blog.com/2012/06/08/autocorrelation-fft-kiss-eigen/
    # https://github.com/stan-dev/math/blob/5f6e8ddd100f00ddf5163c7082ecda077b1e8770/stan/math/prim/mat/fun/autocorrelation.hpp
    centered_signal = x - np.mean(x)
    N = x.size
    M = int(2**np.ceil(np.log2(N)) - N)

    freqvec = np.abs(np.fft.fft(centered_signal, N+M))**2
    ac = np.fft.ifft(freqvec)[:N]

    return np.real(ac/ac[0])


def _autocovariance(x):
    # TODO(ear) test these
    # https://github.com/stan-dev/math/blob/develop/test/unit/math/prim/mat/fun/autocovariance_test.cpp
    ac = autocorrelation(x)
    N = x.size
    return ac * np.var(x) * (N - 1) / N


def autocorrelation(x, color='tab:blue', alpha=1, label='', ax=None, **kws):
    """Draw lag plot.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The location along the x-axis at which the vertical box is placed.

    # TODO(ear) complete doc
    color : string, 'tab:blue' by default
        The color of the box.

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

    x, _, ax = check_data(x, None, ax)

    acor = _autocorrelation(x)

    # TODO(ear) add standard error bars, 1.96/sqrt(len(X))
    for i, ac in np.ndenumerate(acor):
        # TODO(ear) add v/hline
        if ac >= 0:
            ax.vlines(i[0]+1, ymin=0, ymax=ac, color=color, alpha=alpha, label=label, **kws)
        else:
            ax.vlines(i[0]+1, ymin=ac, ymax=0, color=color, alpha=alpha, label=label, **kws)

    return ax
