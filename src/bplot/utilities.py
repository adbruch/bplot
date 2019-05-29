from .check_data import check_data
import matplotlib as mpl
import matplotlib.pyplot as plt

def labels(x="", y="", ax=None, **kws):
    """Set labels."""

    _, _, ax = check_data(None, None, ax)
    if x is not None:
        plt.xlabel(x, **kws)
    if y is not None:
        plt.ylabel(y, **kws)
    return ax


def title(title="", ax=None, **kws):
    """Set title."""

    _, _, ax = check_data(None, None, ax)

    if 'loc' not in kws:
        kws['loc'] = 'left'

    if title is not None:
        plt.title(title, **kws)

    return ax


def subplots(nrows=1, ncols=1, **kws):
    """Get axes for multiple subplots."""

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, **kws)
    return axes

def current_axis(ax=None):
    """Set current axis"""
    plt.sca(ax)
    return ax

def LaTeX(usetex=True):
    """Use LaTeX."""

    plt.rc('text', usetex=usetex)
    return None

def save(filename, ax=None):
    """Save figure."""

    _, _, ax = check_data(None, None, ax)
    plt.tight_layout()
    plt.savefig(filename)
    return ax


def clear(ax=None):
    "Clear axes."

    _, _, ax = check_data(None, None, ax)
    plt.cla()

    return ax


def legend(ax=None, **kws):
    """Make legend."""

    _, _, ax = check_data(None, None, ax)
    plt.legend(**kws)
    return ax
