import matplotlib
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_show_all(ticks, potential, rectangle):
    #plt.axis('equal')
    plt.axes(aspect='equal')

    plt.pcolormesh(ticks[0], ticks[2], np.transpose(potential), zorder=0)
    plt.contour(ticks[0], ticks[2], np.transpose(potential), 20, zorder=1, colors='white', linestyles='solid', linewidths=0.5)
    #plt.contour(ticks[0], ticks[2], np.transpose(potential), zorder=1, colors='black', linestyles='solid')

    # extent = [ticks[0][0], ticks[0][-1], ticks[2][0], ticks[2][-1]]
    # plt.imshow(np.transpose(rectangle), extent=extent, cmap=ListedColormap([[1, 1, 1, 0], [0, 0, 0, 1]]), zorder=2)

    plt.pcolormesh(ticks[0], ticks[2], np.transpose(rectangle), cmap=ListedColormap([[1, 1, 1, 0], [1, 1, 1, 1]]), zorder=2)

    #plt.show()
    plt.savefig('potential.png')


