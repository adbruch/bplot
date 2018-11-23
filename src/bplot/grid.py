from bplot.check_data import check_data

all = ['grid']


def grid(color='grey', linestyle='dashed', ax=None, **kwargs):
    """Draw grid lines."""

    _, _, ax = check_data(None, None, ax)

    ax.grid(True, color=color, linestyle=linestyle, **kwargs)
    return ax
