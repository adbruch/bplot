from .check_data import check_data

all = ['grid']


def grid(below=True, color='grey', linestyle='dashed', ax=None, **kwargs):
    """Draw grid lines."""

    _, _, ax = check_data(None, None, ax)

    ax.set_axisbelow(below)
    out = ax.grid(color=color, linestyle=linestyle, **kwargs)
    return out
