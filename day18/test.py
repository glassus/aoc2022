import matplotlib.pyplot as plt
import numpy as np



x, y, z = np.indices((8, 8, 8))

def cube(xc, yc, zc):
    c = (xc <= x) & (x <= xc) & \
        (yc <= y) & (y <= yc) & \
        (zc <= z) & (z <= zc)
    return c

cube1 = cube(2,3,4)


ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors='red', edgecolor='k')


plt.show()