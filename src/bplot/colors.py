import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

ide = [x for x in range(20) if x % 2 == 0]
ido = [x for x in range(20) if x % 2 == 1]
cmap = plt.get_cmap("tab20")
color = [mpl.colors.to_hex(cmap.colors[x]) for x in ide + ido]

# TODO re-evaluate: Is this the equivalent of
# for i, (name, gdf) in enumerate(carn.groupby("SuperFamily")):
#       bp.color[i]
# If I don't use this in a year, delete it. 2019-08-12
def CatColors(x):
    """A function to convert from a (not necessarily) categorical variable
    to a ndarray of
    """
    u, idx = np.unique(x, return_inverse=True)
    arr_x = np.asarray(color)[idx]
    return arr_x.tolist()


# TODO re-evaluate: What is this from? If I don't use this in a year,
# delete it. 2019-08-12
old_color = [
    "#5D69B1",
    "#E58606",
    "#52BCA3",
    "#99C945",
    "#CC61B0",
    "#24796C",
    "#DAA51B",
    "#2F8AC4",
    "#764E9F",
    "#ED645A",
    "#CC3A8E",
    "#A5AA99",
]

tab_color = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
    "tab:red",
]

# TODO need numerical color gradient
