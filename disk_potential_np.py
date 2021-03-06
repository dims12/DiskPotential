import numpy as np
from tqdm import tqdm
import itertools

import plotting as plt
import space

ticks_np = []
for r, discrete_shape, axis_name in zip(space.ranges, space.shape, space.axis_names):
    tick_np = np.linspace(r[0], r[1], discrete_shape, dtype=np.float32)
    ticks_np.append(tick_np)

x = np.meshgrid(*ticks_np, indexing='ij')
zero_field = np.zeros(space.shape)

y_square = x[1] ** 2
xy_distance_from_center = np.sqrt(x[0] ** 2 + y_square)

density_non_zero = np.logical_and(xy_distance_from_center <= space.disk_radius, np.abs(x[2]) <= space.disk_height)

potential = np.zeros((space.shape[0], space.shape[2]))
for i, k in tqdm(list(itertools.product(range(space.shape[0]), range(space.shape[2])))):
    x_probe = ticks_np[0][i]
    z_probe = ticks_np[2][k]

    distances_from_probe = np.sqrt(
        (x[0] - x_probe) ** 2 + y_square + (x[2] - z_probe) ** 2)

    has_account = np.logical_and(np.not_equal(distances_from_probe, 0), density_non_zero)

    potential_diff = - np.where(has_account, np.divide(1, distances_from_probe), zero_field)

    potential[i][k] = np.sum(potential_diff, axis=None)

j_middle = int(density_non_zero.shape[1] / 2)
density_non_zero_2d = density_non_zero[:, j_middle, :]
plt.plot_show_all(ticks_np, potential, density_non_zero_2d)
