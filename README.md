# Disk Potential

This program demonstrates simple physics computations with Numpy and Tensorflow.

It computes the gravitational potential of thin flat disk and made to dispute with flat 
Earth proponents.

The formula for gravitational potential, generated at location of `r` by mass `M`, located in the origin is following:

![formula for gravitational potential](https://wikimedia.org/api/rest_v1/media/math/render/svg/827549d0dfa4d87471e20fa3a436e0119cf5db99)

`G` is gravitation constant, which I didn't use (set to 1) for simplicity.

To compute potential of a disk, I splitted a space into unit cubes and stored them into `density_non_zero`
3D array. It is `boolean`, so in cubes with `false` there is no mass and there is a mass in cubes
with `true`.

After that, given some probe point, I am computing `potential_diff`, which means contribution of potential 
by each cube. Finally I am summing all contributions and obtaining a potential at that probe point. I am repeating 
this for probe points at cross section with zero `y` and finally have a potential map.

![potential map](potential_sample.png)

Numpy version computes at a speed of `16` iterations per second and takes 15 minute in total on `Intel Core i5-6500 3.2GHz 6Mb `.

Tensorflow GPU version computes at a speed of `210` iterations per second (more than `10` times faster) and takes less than one minute on `8192Mb MSI GeForce GTX 1070 `.

On Amazon `p3.2xlarge` instance with `Tesla V100` it runs at `300` iterations per second.
