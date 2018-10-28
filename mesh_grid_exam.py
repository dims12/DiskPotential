import numpy as np

x = np.arange(-10, 10, 1)
y = np.arange(-5, 5, 1)
z = np.arange(-2, 2, 1)

xx, yy = np.meshgrid(x, y)

print( xx[0:2,0], "Doesn't depend on first argument!" )
print( yy[0,0:2], "Doesn't depend on second argument!" )

xx, yy = np.meshgrid(x, y, indexing='ij')

print( xx[0:2,0], "Now does depend on first argument!" )
print( yy[0,0:2], "Now does depend on second argument!" )

xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')

print( xx[0:2,0,0], "Now does depend on first argument!" )
print( yy[0,0:2,0], "Now does depend on second argument!" )
print( zz[0,0,0:2], "Now does depend on second argument!" )


pass