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
        if not isinstance(x, np.ndarray):
            if isinstance(x, pd.core.series.Series):
                x = x.values
            elif isinstance(x, list):
                x = np.asarray(x)
            elif isinstance(x, (int, float)):
                x = np.asarray([x])
            else:
                raise TypeError(
                    "x must be np.ndarray, pd.core.series.Series, or a list, but is type {}".format(
                        type(x)
                    )
                )

    if y is not None:
        if not isinstance(y, np.ndarray):
            if isinstance(y, pd.core.series.Series):
                y = y.values
            elif isinstance(y, list):
                y = np.asarray(y)
            elif isinstance(y, (int, float)):
                y = np.asarray([y])
            else:
                raise TypeError(
                    "y must be np.ndarray, pd.core.series.Series, or a list, but is type {}".format(
                        type(y)
                    )
                )

    if ax is None:
        ax = plt.gca()

    return x, y, ax
