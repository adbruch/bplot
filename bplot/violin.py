def violins(x, y, color='tab:blue', label=False, ax=None, **kws):
    """Draw violin plots at each value of x."""

    if ax is None:
        ax = plt.gca()

    if color:
        kws['c'] = color
    if label:
        kws['label'] = label

    x_sorted = np.sort(x)
