from .check_data import check_data
import matplotlib as mpl
import matplotlib.pyplot as plt


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


def hide_xaxis(x=True, ax=None):
    """Hide x axis ticks and tick-labels.

    Parameters
    ----------
    x : boolean
        Whether or not to hide the x axis ticks and tick-labels, defaults to True.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the x axis is hidden.  If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.


    Returns
    -------

    ax : matplotlib.pyplot.Axes
         The `Axes` onto which the x axis was hiden.
    """

    _, _, ax = check_data(None, None, ax)
    ax.get_xaxis().set_visible(not x)
    return ax


def hide_yaxis(y=True, ax=None):
    """Hide y axis ticks and tick-labels.

    Parameters
    ----------
    y : boolean
        Whether or not to hide the y axis ticks and tick-labels, defaults to True.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the x axis is hidden.  If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.


    Returns
    -------

    ax : matplotlib.pyplot.Axes
         The `Axes` onto which the x axis was hiden.
    """

    _, _, ax = check_data(None, None, ax)
    ax.get_yaxis().set_visible(not y)
    return ax


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
        ax.set_xlabel(x, **kws)
    if y is not None:
        ax.set_ylabel(y, **kws)
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
    ax.legend().remove()
    plt.legend(**kws)
    return ax


def xticks(ticks=[], labels=None, angle=False, ax=None, **kws):
    """Set x axis ticks.

    Parameters
    ----------
    ticks : array_like
        A list of positions at which ticks should be placed along the x axis,
        defaults to empty list.

    labels : array_like
        A list of explicit labels to place at the given ticks, defaults to
        `None`.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the x axis ticks are set. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    kws : dict
        Arbitrary keyword arguments passed on to
        `matplotlib.pyplot.xticks()`.

    """

    if angle and "rotation" not in kws:
        kws["rotation"] = 30
        kws["ha"] = "right"

    _, _, ax = check_data(None, None, ax)
    plt.xticks(ticks=ticks, labels=labels, **kws)
    return ax


def yticks(ticks=[], labels=None, ax=None, **kws):
    """Set y axis ticks.

    Parameters
    ----------
    ticks : array_like
        A list of positions at which ticks should be placed along the y axis,
        defaults to empty list.

    labels : array_like
        A list of explicit labels to place at the given ticks, defaults to
        `None`.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which the y axis ticks are set. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    kws : dict
        Arbitrary keyword arguments passed on to
        `matplotlib.pyplot.yticks()`.
    """

    _, _, ax = check_data(None, None, ax)
    plt.yticks(ticks=ticks, labels=labels, **kws)
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
    return fig, axes


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

    _, _, ax = check_data(None, None, ax)
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


def dpi(dpi=900):
    """Set figure dots per inch.

    Parameters
    ----------
    dpi : int
        The number of dots per inch of the figure, defaults to 900.

    Returns
    -------
    `None`
    """

    mpl.rcParams["figure.dpi"] = dpi
    return None


def tight_layout(ax=None):
    """Tighten up layout.

    Parameters
    ----------
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
    return ax


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

    ax = tight_layout(ax)
    plt.savefig(filename)
    return ax
