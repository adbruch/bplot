import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def check_data(x=None, y=None, ax=None):
    """Check for valid data.

    Criteria x, y:
    numpy arrays

    shape (N,)
    """

    if x is not None:
        if type(x) is not np.ndarray:
            assert type(x) is pd.core.series.Series
            x = x.values
        if len(x.shape) > 1:
            x = x.reshape((x.shape[0],))

    if y is not None:
        if type(y) is not np.ndarray:
            assert type(y) is pd.core.series.Series
            y = y.values
        if len(y.shape) > 1:
            y = y.reshape((y.shape[0],))

    if ax is None:
        ax = plt.gca()

    return x, y, ax
