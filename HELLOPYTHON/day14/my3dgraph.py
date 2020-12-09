import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')


# test data
x = np.arange(-1., 1., .1)
y = np.arange(-1., 1., .1)
z1 = x + y
z2 = x * x
z3 = -y * y
print(x)
print(x)
# plot test data
ax.plot(x, y, z1)
ax.plot(x, y, z2)
ax.plot(x, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()