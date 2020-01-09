# testing 2d image output libraries
# matplotlib
# this does the basic job: produce and refresh the plot with new data

import numpy as np
import matplotlib.pyplot as plt
import time
# generate figure
fig = plt.figure()
ax = fig.gca()
fig.show()

# refresh plot
for i in range(100):
    plt.cla() # clear axes
    ax.axis('off') # hide x, y axes
    image = np.random.randint(2, size = (100, 100)) # data
    ax.imshow(image, cmap = plt.cm.gray)
    fig.canvas.draw()
    plt.pause(0.1)
    