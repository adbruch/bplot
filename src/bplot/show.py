import matplotlib.pyplot as plt

def show(*args, **kws):
  """Show a window with the given plot data. Blocks until window is closed.

  Parameters
  ----------
  *args : pyplot args
  **kws : pyplot kw

  Examples
  --------
  Plot a line.

        >>> bplot.line(x, y)
        >>> bplot.show()
  """
  plt.show(*args, **kws)
