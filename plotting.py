import matplotlib
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_float(ticks, density):
    # x = [ticks[0][0], ticks[0][-1]]
    # z = [ticks[2][0], ticks[2][-1]]
    plt.pcolormesh(ticks[0], ticks[2], np.transpose(density), zorder=0)
    plt.contour(ticks[0], ticks[2], np.transpose(density), zorder=1, colors='black', linestyles='solid')


def plot_bool(ticks, density):
    extent = [ticks[0][0], ticks[0][-1], ticks[2][0], ticks[2][-1]]
    plt.imshow(np.transpose(density), extent=extent, cmap=ListedColormap([[1, 1, 1, 0], [0, 0, 0, 1]]), zorder=2)


def plot_show_all(ticks, potential, rectangle):
    plot_float(ticks, potential)
    plot_bool(ticks, rectangle)
    plt.show()


