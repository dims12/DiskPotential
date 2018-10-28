import numpy as np

x = np.arange(-2, 2, 1)
y = np.arange(-2, 2, 1)
z = np.arange(-2, 2, 1)

xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')
