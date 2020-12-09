import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

z=np.linspace(0,30,100)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z)

# make labels

plt.show()







