import math
import numpy as np
from tqdm import tqdm

width = 1000
depth = 1000
height = 20
R0 = 500
hz = 1

x = np.arange(-width, width, 1)
y = np.arange(-depth, depth, 1)
z = np.arange(-height, height, 1)

xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')

r_xy = np.sqrt(xx ** 2 + yy ** 2)

density = ((r_xy <= R0) & (-hz <= zz) & (zz <= hz)).astype(np.double)


def potential_f(x1, z1):
    # xzeros = np.nonzero(np.power(xx - x1, 2)==0)
    # yzeros = np.nonzero(np.power(yy, 2)==0)
    # zzeros = np.nonzero(np.power(zz - z1, 2) == 0)
    r = np.sqrt(np.power(xx - x1, 2) + np.power(yy, 2) + np.power(zz - z1, 2))

    # rzeros = np.nonzero(r == 0)
    phi = - density / r
    phi[np.isinf(phi) | np.isnan(phi)] = 0
    return np.sum(phi, axis=None)


potential = np.zeros((width*2, height*2))

for i1 in tqdm(range(width * 2)):
    for k1 in range(height+1, height * 2):
        xxx = x[i1]
        zzz = z[k1]
        p = potential_f(xxx, zzz)
        potential[i1, k1] = p

pass
