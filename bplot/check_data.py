import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

all = ['check_data']


def check_data(x=None, y=None, ax=None):
    """Check for valid data."""

    if x is not None and type(x) is not np.ndarray:
        assert type(x) is pd.core.series.Series
        x = x.values

    if y is not None and type(y) is not np.ndarray:
        assert type(y) is pd.core.series.Series
        y = y.values

    if ax is None:
        ax = plt.gca()

    return x, y, ax
