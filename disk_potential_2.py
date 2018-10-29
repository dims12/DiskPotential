import tensorflow as tf
import numpy as np
from tqdm import tqdm
import itertools

axis_names = 'xyz'
space_discrete_shape = (2000, 2000, 20)
space_range = (
    np.array([-1000, 1000], dtype=np.float32),  # x
    np.array([-1000, 1000], dtype=np.float32),  # y
    np.array([-10, 10], dtype=np.float32)  # z
)

disk_radius = 500
disk_height = 2

ticks_np = []
for r, discrete_shape, axis_name in zip(space_range, space_discrete_shape, axis_names):
    tick_np = np.linspace(r[0], r[1], discrete_shape, dtype=np.float32)
    ticks_np.append(tick_np)

x = tf.meshgrid(*ticks_np, indexing='ij')
zero_field = tf.zeros(space_discrete_shape)

y_square = x[1] * x[1]
xy_distance_from_center = tf.sqrt(x[0] * x[0] + y_square, name='xy_distance_from_center')

density_non_zero = tf.logical_and(xy_distance_from_center <= disk_radius, tf.abs(x[2]) <= disk_height, name='density')

x_probe = tf.get_variable('x_probe', shape=(), dtype=tf.float32)
z_probe = tf.get_variable('z_probe', shape=(), dtype=tf.float32)

distances_from_probe = tf.sqrt(
    tf.squared_difference(x[0], x_probe) + y_square + tf.squared_difference(x[2], z_probe))

has_account = tf.logical_and(tf.not_equal(distances_from_probe, 0), density_non_zero)

potential_diff = - tf.where(has_account, np.divide(1, distances_from_probe), zero_field)
potential = tf.reduce_sum(potential_diff, axis=None)

potential_np = np.zeros((space_discrete_shape[0], space_discrete_shape[2]))
with tf.Session() as sess:
    sess.run([density_non_zero, zero_field])
    for i, k in tqdm(list(itertools.product(range(space_discrete_shape[0]), range(space_discrete_shape[2])))):
        xx = ticks_np[0][i]
        zz = ticks_np[2][k]
        p = sess.run(potential, feed_dict={x_probe: xx, z_probe: zz})
        potential_np[i][k] = p
