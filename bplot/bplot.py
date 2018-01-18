import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import functools
import inspect
import pandas as pd

__all__ = ['BPlot']


class BPlot(object):

    def __init__(self, data=None, *args, **kws):
        # TODO(ear) does this work well?
        if kws is None:
            kws = dict()
        kws.setdefault('ncols', 1)
        kws.setdefault('nrows', 1)
        kws.setdefault('figsize', (4.5, 4.5))

        self.fig, self.axes = plt.subplots(*args, **kws)

        # store first input
        self._x = None
        self._y = None
        if data is not None:
            self._data = data.copy()

        # set few, simple customs
        for item in ([
                self.axes.title,
                self.axes.xaxis.label,
                self.axes.yaxis.label] +
                self.axes.get_xticklabels() + self.axes.get_yticklabels()):
            item.set_fontsize(14)

        local_methods = self.__dir__()

        # allow chaining of matplotlib.axes.Axes by
        # dynamically binding wrapped versions of axes' methods
        # such that each is not already redefined locally
        for key, value in inspect.getmembers(self.axes):
            if inspect.ismethod(value) and key not in local_methods:
                bound_fn = functools.partial(self._axes_method, key)
                setattr(self, key, bound_fn)



    # wrapper around axes' methods
    def _axes_method(self, f, *args, **kws):
        """Wraps ``matplotlib.axes.Axes``'s methods to allow for method chaining."""
        method = getattr(self.axes, f, None)
        if method is not None:
            method(*args, **kws)
        return self


    # def tight_layout(self):
    #     """TODO (ear) verify: Wraps ``matplotlib.plt.tight_layout()``'s tight_layout."""
    #     # unclear how this might affect multiple open plots
    #     plt.tight_layout()
    #     return self


    # def savefig(self, *args, **kws):
    #     """TODO (ear) verify: Wraps ``matplotlib.plt.savefig()``'s savefig."""
    #     plt.savefig(*args, **kws)
    #     return self


    def tick_params(self, *args, **kws):
        """A wrapper around ``matplotlib.axes.Axes.tick_params``."""

        self.axes.tick_params(*args, **kws)
        return self


    def title_set_fontsize(self, *args, **kws):
        """A wrapper around ``matplotlib.axes.Axes.title.set_fontsize``."""

        self.axes.title.set_fontsize(*args, **kws)
        return self


    def xaxis_set_fontsize(self, *args, **kws):
        """A wrapper around ``matplotlib.axes.Axes.xaxis.label.set_fontsize``."""

        self.axes.xaxis.label.set_fontsize(*args, **kws)
        return self


    def yaxis_set_fontsize(self, *args, **kws):
        """A wrapper around ``matplotlib.axes.Axes.yaxis.label.set_fontsize``."""

        self.axes.yaxis.label.set_fontsize(*args, **kws)
        return self


    def histogram(self, x=None, data=None, **kws):
        """Draw a histogram.

        A wrapper around ``matplotlib.axes.Axes.hist``.

        """

        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if isinstance(x, str):
            if x not in data.columns:
                raise KeyError('{0} is not found in {1}'.format(x, data.columns))

            self.axes.hist(data[x].values, **kws)

        self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        return self


    def density(self, x=None, group=None, color=False, data=None,
                label=False, n=101, bw_method=None, **kws):
        """Draw density plot.

        Group data stored in ``x`` by ``group``.

        Color grouped data, default ``False``.

        """

        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if isinstance(x, str):
            if x not in data.columns:
                raise KeyError('{0} is not found in {1}'.format(x, data.columns))


        data_min = data[x].min()
        data_max = data[x].max()
        xs = np.linspace(data_min, data_max, n)

        if group is not None:

            if isinstance(group, str):
                if group not in data.columns:
                    raise KeyError('{0} is not found in {1}'.format(group, data.columns))

            data_grouped = data.groupby(group)
            if color:
                cols = mpl.cm.tab20(np.linspace(0, 1, data_grouped.ngroups))

            for i, (name, group) in enumerate(data_grouped):
                density = stats.kde.gaussian_kde(group[x].values.ravel(), bw_method)
                if color:
                    kws['c'] = cols[i]
                if label:
                    kws['label'] = name
                self.axes.plot(xs, density(xs), **kws)

        else:

            density = stats.kde.gaussian_kde(data[x].values.ravel(), bw_method)
            self.axes.plot(xs, density(xs), **kws)

        self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        return self


    def violin(self, x=None, y=None, data=None, **kws):
        """A wrapper around ``matplotlib.axes.Axes.violinplot``.

        If ``x`` contains data then ``y`` can be used as a grouping variable and the violins will be horizontal.  If ``y`` contains data then ``x`` can be used as a grouping variable and the violins will be vertical.
        """

        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if y is None and self._y is not None:
            y = self._y
        else:
            self._y = y


        if isinstance(x, str) and isinstance(y, str):
            assert x in data.columns
            assert y in data.columns

            nx = data[x].nunique()
            ny = data[y].nunique()
            if nx > ny:
                # horizontal violin plots
                if kws is None:
                    kws = dict()
                kws.setdefault('vert', False)

                df_sorted = data.sort_values(y)
                df_sorted_grouped = df_sorted.groupby(y)
                positions = np.arange(ny)

                data_x_seq = [None]*df_sorted_grouped.ngroups
                for i, (name, group) in enumerate(df_sorted_grouped):
                    data_x_seq[i] = group[x]

                self.axes.violinplot(data_x_seq, positions, **kws)

                self.axes.set_ylim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_yticks(positions)
                self.axes.set_yticklabels(
                    list(df_sorted_grouped.groups.keys())
                )
            else:
                # vertical violin plots
                df_sorted = data.sort_values(x)
                df_sorted_grouped = df_sorted.groupby(x)
                positions = np.arange(nx)

                data_y_seq = [None]*df_sorted_grouped.ngroups
                for i, (name, group) in enumerate(df_sorted_grouped):
                    data_y_seq[i] = group[y]

                self.axes.violinplot(data_y_seq, positions, **kws)

                self.axes.set_xlim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_xticks(positions)
                self.axes.set_xticklabels(
                    list(df_sorted_grouped.groups.keys())
                )


            self.axes.set_ylabel(y.capitalize().replace('_', ' '))
            self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        return self


    def rug(self, x, y=0, kws_plot=None):
        """Draw rug."""

        if kws_plot is None:
            kws_plot = dict()
        kws_plot.setdefault('color', 'k')
        kws_plot.setdefault('marker', '|')
        kws_plot.setdefault('linestyle', '')

        self.axes.plot(x, [y]*len(x), **kws_plot)

        return self


    def std_interval(self, x=None, y=None, data=None,
                          confidence=0.95, kws_plot=None, kws_lines=None):
        """Draw a thin interval based using the sample standard deviation.

        The interval is horizontal/vertical, centered by mean and y/x.

        """

        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if y is None and self._y is not None:
            y = self._y
        else:
            self._y = y


        if kws_plot is None:
            kws_plot = dict()
        kws_plot.setdefault('color', 'white')
        kws_plot.setdefault('zorder', 3)
        kws_plot.setdefault('mew', 2)
        kws_plot.setdefault('ms', 7)


        if kws_lines is None:
            kws_lines = dict()
        kws_lines.setdefault('color', 'k')
        kws_lines.setdefault('linestyle', '-')
        kws_lines.setdefault('lw', 1)

        lower_area = 1 - (1-confidence)/2
        zstar = stats.norm.ppf(lower_area)

        if (isinstance(x, str) and isinstance(y, str)):
            assert x in data.columns
            assert y in data.columns

            nx = data[x].nunique()
            ny = data[y].nunique()
            if nx > ny:
                # horizonal std_intervals
                df_sorted = data.sort_values(y)
                df_sorted_grouped = df_sorted.groupby(y)
                positions = np.arange(ny)
                kws_plot.setdefault('marker', '|')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    group_x = group[x]
                    mean = group_x.mean()
                    std = group_x.std()
                    lb = mean - zstar*std
                    ub = mean + zstar*std
                    self.axes.plot(mean, positions[i], **kws_plot)
                    self.axes.hlines(positions[i], lb, ub, **kws_lines)


                self.axes.set_ylim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_yticks(positions)
                self.axes.set_yticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

            else:
                # vertical std_intervals
                df_sorted = data.sort_values(x)
                df_sorted_grouped = df_sorted.groupby(x)
                positions = np.arange(nx)
                kws_plot.setdefault('marker', '|')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    group_y = group[y]
                    mean = group_y.mean()
                    std = group_y.std()
                    lb = mean - zstar*std
                    ub = mean + zstar*std
                    self.axes.plot(positions[i], mean, **kws_plot)
                    self.axes.vlines(positions[i], lb, ub, **kws_lines)

                self.axes.set_xlim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_xticks(positions)
                self.axes.set_xticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        elif isinstance(x, str) and isinstance(y, float):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))

            kws_plot.setdefault('marker', '|')

            data_x = data[x]
            mean = data_x.mean()
            ste = data_x.std()
            lb = mean - zstar*ste
            ub = mean + zstar*ste

            self.axes.hlines(y, lb, ub, **kws_lines)
            self.axes.plot(mean, y, **kws_plot)

        elif isinstance(x, float) and isinstance(y, str):
            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))

            data_y = data[y]
            mean = data_y.mean()
            ste = data_y.std()
            lb = mean - zstar*ste
            ub = mean + zstar*ste

            self.axes.vlines(x, lb, ub, **kws_lines)
            self.axes.plot(x, mean, **kws_plot)

        return self


    def ste_interval(self, x=None, y=None, data=None,
                     confidence=0.95, kws_plot=None, kws_lines=None):
        """Draw a thin interval based using the sample standard error.

        The interval is horizontal/vertical, centered by mean and y/x.

        """

        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if y is None and self._y is not None:
            y = self._y
        else:
            self._y = y


        if kws_plot is None:
            kws_plot = dict()
        kws_plot.setdefault('color', 'white')
        kws_plot.setdefault('zorder', 3)
        kws_plot.setdefault('mew', 2)
        kws_plot.setdefault('ms', 7)


        if kws_lines is None:
            kws_lines = dict()
        kws_lines.setdefault('color', 'k')
        kws_lines.setdefault('linestyle', '-')
        kws_lines.setdefault('lw', 1)

        lower_area = 1 - (1-confidence)/2
        zstar = stats.norm.ppf(lower_area)

        if (isinstance(x, str) and isinstance(y, str)):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))
            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))

            nx = data[x].nunique()
            ny = data[y].nunique()
            if nx > ny:
                # horizonal std_intervals
                df_sorted = data.sort_values(y)
                df_sorted_grouped = df_sorted.groupby(y)
                positions = np.arange(ny)
                kws_plot.setdefault('marker', '|')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    group_x = group[x]
                    mean = group_x.mean()
                    ste = group_x.std()/np.sqrt(group_x.shape[0])
                    lb = mean - zstar*ste
                    ub = mean + zstar*ste
                    self.axes.plot(mean, positions[i], **kws_plot)
                    self.axes.hlines(positions[i], lb, ub, **kws_lines)

                self.axes.set_ylim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_yticks(positions)
                self.axes.set_yticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

            else:
                # vertical std_intervals
                df_sorted = data.sort_values(x)
                df_sorted_grouped = df_sorted.groupby(x)
                positions = np.arange(nx)
                kws_plot.setdefault('marker', '|')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    group_y = group[y]
                    mean = group_y.mean()
                    ste = group_y.std()/np.sqrt(group_x.shape[0])
                    lb = mean - zstar*ste
                    ub = mean + zstar*ste
                    self.axes.plot(positions[i], mean, **kws_plot)
                    self.axes.vlines(positions[i], lb, ub, **kws_lines)

                self.axes.set_xlim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_xticks(positions)
                self.axes.set_xticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        elif isinstance(x, str) and isinstance(y, float):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))

            kws_plot.setdefault('marker', '|')

            data_x = data[x]
            mean = data_x.mean()
            ste = data_x.std()/np.sqrt(data_x.shape[0])
            lb = mean - zstar*ste
            ub = mean + zstar*ste

            self.axes.hlines(y, lb, ub, **kws_lines)
            self.axes.plot(mean, y, **kws_plot)

        elif isinstance(x, float) and isinstance(y, str):
            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))

            data_y = data[y]
            mean = data_y.mean()
            ste = data_y.std()/np.sqrt(data_y.shape[0])
            lb = mean - zstar*ste
            ub = mean + zstar*ste

            self.axes.vlines(x, lb, ub, **kws_lines)
            self.axes.plot(x, mean, **kws_plot)

        return self


    def _bx(self, _x):
        """Compute five numbers for box plot."""
        q1, q2, q3 = np.percentile(_x, [25, 50, 75])
        iqr = q3 - q1

        _x_min = _x.min()
        _x_max = _x.max()

        uw = q3 + iqr * 1.5
        uw = np.clip(uw, q3, _x_max)

        lw = q1 - iqr * 1.5
        lw = np.clip(lw, _x_min, q1)

        return q1, q2, q3, lw, uw


    def box(self, x=None, y=None, data=None,
            kws_plot=None, kws_lines=None):
        """Draw a box plot.

        The interval is horizontal/vertical, centered by median and y/x.

        """

        # TODO(ear) moar sanity checks
        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if y is None and self._y is not None:
            y = self._y
        else:
            self._y = y


        if kws_plot is None:
            kws_plot = dict()
        kws_plot.setdefault('color', 'w')
        kws_plot.setdefault('zorder', 3)
        kws_plot.setdefault('mew', 3)
        kws_plot.setdefault('ms', 7)


        if kws_lines is None:
            kws_lines = dict()
        kws_lines.setdefault('color', 'k')
        kws_lines.setdefault('linestyle', '-')
        kws_lines.setdefault('lw', 1)

        if isinstance(x, str) and isinstance(y, str):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))
            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))

            nx = data[x].nunique()
            ny = data[y].nunique()
            if nx > ny:
                # horizontal box plots
                df_sorted = data.sort_values(y)
                df_sorted_grouped = df_sorted.groupby(y)
                positions = np.arange(ny)
                kws_plot.setdefault('marker', '|')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    q1, q2, q3, lw, uw = self._bx(group[x])
                    self.axes.hlines(positions[i], lw, uw, **kws_lines)
                    kws_lines['lw'] += 4
                    self.axes.hlines(positions[i], q1, q3, **kws_lines)
                    kws_lines['lw'] -= 4
                    self.axes.plot(q2, positions[i], **kws_plot)


                self.axes.set_ylim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_yticks(positions)
                self.axes.set_yticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

            else:
                # vertical box plots
                df_sorted = data.sort_values(x)
                df_sorted_grouped = df_sorted.groupby(x)
                positions = np.arange(nx)
                kws_plot.setdefault('marker', '_')

                for i, (name, group) in enumerate(df_sorted_grouped):
                    q1, q2, q3, lw, uw = self._bx(group[y])
                    self.axes.plot(positions[i], q2, **kws_plot)
                    self.axes.vlines(positions[i], lw, uw, **kws_lines)
                    kws_lines['lw'] += 4
                    self.axes.vlines(positions[i], q1, q3, **kws_lines)
                    kws_lines['lw'] -= 4

                self.axes.set_xlim([positions[0]-0.5, positions[-1]+0.5])
                self.axes.set_xticks(positions)
                self.axes.set_xticklabels(
                    list(df_sorted_grouped.groups.keys())
                )

                self.axes.set_ylabel(y.capitalize().replace('_', ' '))
                self.axes.set_xlabel(x.capitalize().replace('_', ' '))

        elif isinstance(x, str) and isinstance(y, float):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))

            kws_plot.setdefault('marker', '|')

            q1, q2, q3, lw, uw = self._bx(data[x])
            self.axes.hlines(y, lw, uw, **kws_lines)
            kws_lines['lw'] += 4
            self.axes.hlines(y, q1, q3, **kws_lines)
            kws_lines['lw'] -= 4
            self.axes.plot(q2, y, **kws_plot)


        elif isinstance(x, float) and isinstance(y, str):
            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))

            kws_plot.setdefault('marker', '_')

            q1, q2, q3, lw, uw = self._bx(data[x])
            self.axes.vlines(x, lw, uw, **kws_lines)
            kws_lines['lw'] += 4
            self.axes.vlines(x, q1, q3, **kws_lines)
            kws_lines['lw'] -= 4
            self.axes.plot(x, q2, **kws_plot)


        else:
            raise ValueError('{0} and/or {1} not handled.'.format(x, y))


        return self


    def points(self, x=None, y=None, data=None,
               color=None, kws=None):
        """Draw a scatter plot."""

        # TODO(ear) moar sanity checks
        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()

        if x is None and self._x is not None:
            x = self._x
        else:
            self._x = x

        if y is None and self._y is not None:
            y = self._y
        else:
            self._y = y


        if kws is None:
            kws = dict()
        kws.setdefault('color', 'b')

        if isinstance(x, str) and isinstance(y, str):
            assert x in data.columns
            assert y in data.columns

            if color is not None and isinstance(color, str):
                assert color in data.columns

                df_grouped = data.groupby(color)
                ngroups = df_grouped.ngroups
                cols = mpl.cm.tab20(np.linspace(0, 1, ngroups))

                for i, (name, group) in enumerate(df_grouped):
                    kws['c'] = cols[i]
                    kws['label'] = name
                    self.axes.scatter(group[x], group[y], **kws)

            else:

                self.axes.scatter(data[x], data[y], **kws)

        self.axes.set_ylabel(y.capitalize().replace('_', ' '))
        self.axes.set_xlabel(x.capitalize().replace('_', ' '))


        return self


    def line(self, x=None, y=None, data=None,
             color=None, kws=None):
        """Plot line."""

        # TODO(ear) moar sanity checks
        if data is None:
            data = self._data.copy()
        else:
            self._data = data.copy()


        if kws is None:
            kws = dict()
        kws.setdefault('c', 'k')

        if isinstance(x, str) and isinstance(y, str):
            if x not in data.columns:
                raise KeyError('{0} not found in {1}'.format(x, data.columns))

            if y not in data.columns:
                raise KeyError('{0} not found in {1}'.format(y, data.columns))


            if color is not None and isinstance(color, str):
                if color not in data.columns:
                    raise KeyError('{0} not found in {1}'.format(color, data.columns))

                df_grouped = data.groupby(color)
                ngroups = df_grouped.ngroups
                cols = mpl.cm.tab20(np.linspace(0, 1, ngroups))

                for i, (name, group) in enumerate(df_grouped):
                    kws['c'] = cols[i]
                    kws['label'] = name
                    self.axes.plot(group[x], group[y], **kws)

            else:

                self.axes.plot(data[x], data[y], **kws)

        self.axes.set_ylabel(y.capitalize().replace('_', ' '))
        self.axes.set_xlabel(x.capitalize().replace('_', ' '))

# TODO(ear) colors, facets

# TODO(ear) All x,y input strings from a dataframe?
# if no, add new input forms
# x column name, y length 1 list
# x=[numbers], y=[1]
# x=[numbers], y=None => y=[0]
# y column name, x length 1 list
# y=[numbers], x=[1]
# y=[numbers], x=None => x=[0]
# x=[numbers], y=[a few numbers, specific positions]
# y=[numbers], x=[a few numbers, specific positions]
