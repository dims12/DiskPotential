import numpy as np

disk_radius = 100
disk_height = 1

voxels_per_unit = 1

x_range = [-disk_radius*2, disk_radius*2]
y_range = [-disk_radius*2, disk_radius*2]
z_range = [-disk_radius/5, disk_radius/5]

axis_names = 'xyz'
shape = (
    int((x_range[1] - x_range[0]) * voxels_per_unit),
    int((y_range[1] - y_range[0]) * voxels_per_unit),
    int((z_range[1] - z_range[0]) * voxels_per_unit)
)
ranges = (
    np.array(x_range, dtype=np.float32),  # x
    np.array(y_range, dtype=np.float32),  # y
    np.array(z_range, dtype=np.float32)  # z
)


