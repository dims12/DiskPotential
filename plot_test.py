import matplotlib
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

x_ticks = np.linspace(-10, 10, 100, dtype=np.float32)
y_ticks = np.linspace(-10, 10, 100, dtype=np.float32)

x, y = np.meshgrid(x_ticks, y_ticks, indexing='ij')

# density plot of some circular function
r = np.sqrt(x ** 2 + y ** 2)
z = np.where(r != 0, np.sin(r) / r, 1)

plt.figure(1)
plt.pcolormesh(x_ticks, y_ticks, z)
rectangle = np.logical_and(np.abs(x) < 2,  np.abs(y) < 2)
extent = [x_ticks[0], x_ticks[-1], y_ticks[0], y_ticks[-1]]
plt.imshow(rectangle, extent=extent, cmap=ListedColormap([[1, 1, 1, 0], [0, 0, 0, 1]]), zorder=1)
plt.show()

