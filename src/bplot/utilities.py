from .check_data import check_data
import matplotlib as mpl
import matplotlib.pyplot as plt


def labels(x="", y="", ax=None, **kws):
    """Set axis labels.

    Parameters
    ----------
    x : string
        The label to be set on x axis.

    y : string
        The label to be set on the y axis.

    kws : dict
        Arbitrary keyword arguments passed on to
        `matplotlib.pyplot.xlabel()` and `matplotlib.pyplot.ylabel()`.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the labels are set.  If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.


    Returns
    -------

    ax : `matplotlib.pyplot.Axes`
         The `Axes` onto which the axis labels are set.
    """

    _, _, ax = check_data(None, None, ax)
    if x is not None:
        plt.xlabel(x, **kws)
    if y is not None:
        plt.ylabel(y, **kws)
    return ax


def title(title="", ax=None, **kws):
    """Set title, defaults to left justified, `loc='left'`.

    Parameters
    ----------
    title : string
            The label to be set on as the title.

    kws : dict
          Arbitrary keyword arguments passed on to
          `matplotlib.pyplot.title()`.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the labels are set.  If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.


    Returns
    -------

    ax : matplotlib.pyplot.Axes
         The `Axes` onto which the title is set.
    """

    _, _, ax = check_data(None, None, ax)

    if "loc" not in kws:
        kws["loc"] = "left"

    if title is not None:
        plt.title(title, **kws)

    return ax


def subplots(nrows=1, ncols=1, **kws):
    """Get axes for multiple subplots.

    Parameters
    ----------
    nrows : int
            The desired number of rows in the multi-plot figure.

    ncols : int
            The desired number of columns in the multi-plot figure.

    kws : dict
          Arbitrary keyword arguments passed on to
          `matplotlib.pyplot.subplots()`.

    Returns
    -------

    ax : `matplotlib.pyplot.Axes`
         The `Axes` onto which the plots will be drawn.
    """

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, **kws)
    return axes


def current_axis(ax=None):
    """Set current axis.

    Parameters
    ----------
    ax : `matplotlib.pyplot.Axes`
        The `Axes` onto which the box

    Returns
    -------

    ax : matplotlib.pyplot.Axes
         The `Axes` onto which the plot will be drawn.
    """

    plt.sca(ax)
    return ax


def LaTeX(usetex=True):
    """Use LaTeX.

    Parameters
    ----------
    usetex : boolean
        Whether or not to use LaTeX in plots, defaults to `True`.

    Returns
    -------

    `None`
    """

    plt.rc("text", usetex=usetex)
    return None


def save(filename, ax=None):
    """Save figure.

    Parameters
    ----------
    filename : string
        The filepath into which the current figure will be saved.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis from which the plot to be saved derives. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    Returns
    -------

    ax : matplotlib.pyplot.Axes
         The `Axes` for which the plot was saved.
    """

    _, _, ax = check_data(None, None, ax)
    plt.tight_layout()
    plt.savefig(filename)
    return ax


def clear(ax=None):
    """Clear axes.

    Parameters
    ----------
    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis to be cleared. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    Returns
    -------
    ax : matplotlib.pyplot.Axes
         The `Axes` that was cleared.
    """

    _, _, ax = check_data(None, None, ax)
    plt.cla()

    return ax


def legend(ax=None, **kws):
    """Make legend.

    Parameters
    ----------
    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which a legend is set. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    kws : dict
        Arbitrary keyword arguments passed to `matplotlib.pyplot.legend()`.

    Returns
    -------
    ax : matplotlib.pyplot.Axes
         The `Axes` onto which the legend was drawn.
    """

    _, _, ax = check_data(None, None, ax)
    plt.legend(**kws)
    return ax
