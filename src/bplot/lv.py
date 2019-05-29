# Modified from https://github.com/mwaskom/seaborn
# specifically from
# https://github.com/mwaskom/seaborn/blob/master/seaborn/categorical.py
# under BSD-3 license

all = ["lv"]

from bplot.check_data import check_data

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as Patches
from matplotlib.collections import PatchCollection
import numpy as np
from scipy import stats


def lv(
    x,
    y,
    color="tab:blue",
    label="",
    widths=0.8,
    p=0.007,
    scale="linear",
    k_depth="proportion",
    ax=None,
):
    """Draw vertical letter value plot.

    Parameters
    ----------
    x : int
        The location along the x-axis at which the vertical letter value plot is placed.

    y : {numpy.array, pandas.core.series.Series}
        The vector of data for which the percentiles are sought.

    color : string, 'tab:blue' by default
        The color of the boxes.

    label : string, '' (empty) by default
        The label within a potential legend.

    widths : float, 0.8 by default
        The width of the median box.

    scale : string, 'linear' by default
        Options are exponential, linear, or area.

    k_depth : string, 'proportion' by default
        Options are proportion, tukey, or trustworthy.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the letter value plot is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    _, y, ax = check_data(None, y, ax)
    if ax is None:
        ax = plt.gca()

    n = y.size
    k_dict = {
        "proportion": (np.log2(n)) - int(np.log2(n * p)) + 1,
        "tukey": (np.log2(n)) - 3,
        "trustworthy": (np.log2(n) - np.log2(2 * stats.norm.ppf((1 - p)) ** 2)) + 1,
    }
    k = k_dict[k_depth]
    try:
        k = int(k)
    except ValueError:
        k = 1
    # If the number happens to be less than 0, set k to 0
    if k < 1.0:
        k = 1

    upper = [100 * (1 - 0.5 ** (i + 2)) for i in range(k, -1, -1)]
    lower = [100 * (0.5 ** (i + 2)) for i in range(k, -1, -1)]
    # Stitch the box ends together
    percentile_ends = [(i, j) for i, j in zip(lower, upper)]
    box_ends = [np.percentile(y, q) for q in percentile_ends]

    # Dictionary of functions for computing the width of the boxes
    width_functions = {
        "linear": lambda h, i, k: (i - 1.0) / k,
        "exponential": lambda h, i, k: 2 ** (-k + i - 1),
        "area": lambda h, i, k: (1 - 2 ** (-k + i - 2)) / h,
    }

    # Anonymous functions for calculating the width and height
    # of the letter value boxes
    width = width_functions[scale]

    # Function to find height of boxes
    def height(b):
        return b[1] - b[0]

    # Functions to construct the letter value boxes
    def vert_perc_box(x, b, i, k, w):
        rect = Patches.FancyBboxPatch(
            (x - widths * w / 2, b[0]),
            widths * w,
            height(b),
            fill=True,
            boxstyle="round,pad=0.05",
        )
        return rect

    def horz_perc_box(x, b, i, k, w):
        rect = Patches.Rectangle(
            (b[0], x - widths * w / 2), height(b), widths * w, fill=True
        )
        return rect

    # Scale the width of the boxes so the biggest starts at 1
    w_area = np.array([width(height(b), i, k) for i, b in enumerate(box_ends)])
    w_area /= np.max(w_area)

    # Calculate the median
    median_y = np.median(y)

    # Calculate the outliers and plot
    perc_ends = (100 * (0.5 ** (k + 2)), 100 * (1 - 0.5 ** (k + 2)))
    edges = np.percentile(y, perc_ends)
    lower_out = y[np.where(y < edges[0])[0]]
    upper_out = y[np.where(y > edges[1])[0]]
    outliers = np.concatenate((lower_out, upper_out))

    boxes = [
        vert_perc_box(x, b[0], i, k, b[1]) for i, b in enumerate(zip(box_ends, w_area))
    ]

    # Plot the medians
    half_width = boxes[k].get_extents().width / 2
    ax.plot([x - half_width, x + half_width], [median_y, median_y], c=".15", alpha=0.45)

    # Plot the outliers
    color = mpl.colors.to_hex(color)
    ax.scatter(np.repeat(x, len(outliers)), outliers, marker="*", c=color)

    rgb = [[1, 1, 1], mpl.colors.to_rgb(color)]
    cmap = mpl.colors.LinearSegmentedColormap.from_list("new_map", rgb)
    collection = PatchCollection(boxes[1:], cmap=cmap, edgecolors=([0, 0, 0, 0.45],))
    collection.set_array(np.array(np.linspace(0, 1, len(boxes))))
    ax.add_collection(collection)

    return ax


# TODO lv_h: minimize duplicate code
