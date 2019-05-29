from bplot.check_data import check_data
import matplotlib.pyplot as plt


def grid(b=True, ax=None, **kws):
    """Show grid lines.
    Parameters
    ----------
    b : boolean
        Whether or not to draw grid, defaults to `True`.

    ax : `matplotlib.pyplot.Axes`, `None` by default
        The axis onto which a grid is drawn. If left as `None`,
        `matplotlib.pyplot.gca()` is called to get the current `Axes`.

    kws : dict
        Arbitrary keyword arguments passed to `matplotlib.pyplot.grid()`.

    Returns
    -------
    ax : matplotlib.pyplot.Axes
         The `Axes` onto which a grid was drawn.
    """

    _, _, ax = check_data(None, None, ax)

    if "alpha" not in kws:
        kws["alpha"] = 0.25
    plt.grid(b=b, **kws)
    return ax
