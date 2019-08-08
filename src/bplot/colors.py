import matplotlib.pyplot as plt
import matplotlib as mpl

color = [
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
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
]

ide = [x for x in range(20) if x % 2 == 0]
ido = [x for x in range(20) if x % 2 == 1]
cmap = plt.get_cmap("tab20")
cat_color = [mpl.colors.to_hex(cmap.colors[x]) for x in ide + ido]
