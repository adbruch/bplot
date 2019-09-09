import matplotlib.pyplot as plt

def show(*data):
  """Show a window with the given plot data. Blocks until window is closed.

  Parameters
  ----------
  *data : indexable objects
      An object with labelled data. (Axes, Line2D, Line2D list, etc...)

  Examples
  --------
    The returned values from most bplot functions can be plotted.

        >>> bplot.show(bplot.line(x, y))

    Plot multiple lines at once.

        >>> bplot.show(bplot.line(x1, y1), bplot.line(x2, y2))
  """
  for d in data:
    plt.plot(data=d)
  plt.show()
