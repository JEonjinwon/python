import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

def z_functinon(x,y):
    return np.sin(np.sqrt(x**2+y**2))
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

X, Y=np.msehgrid(x,y)
Z=z_functinon(X,Y)

ax.plot_surface(X,Y,Z)


plt.show()







