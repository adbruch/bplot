from bplot.check_data import check_data
import matplotlib.pyplot as plt


def grid(b=True, ax=None, **kws):
    """Show grid lines."""

    _, _, ax = check_data(None, None, ax)

    if 'alpha' not in kws:
        kws['alpha'] = 0.25
    plt.grid(b=b, **kws)
    return ax
