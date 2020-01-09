# exploring 3d plotting

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate figure
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# refresh plot
for i in range(100):
    plt.cla() # clear axes
    ax.axis('off') # hide x, y axes
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = np.random.rand(100)
    z = (z - np.nanmin(z)) / (np.nanmax(z) - np.nanmin(z))
    ax.scatter(x, y, z, cmap = 'hot', c = z)
    fig.canvas.draw()
    plt.pause(0.1)
    