# Conway's game of life
# This thing has a simple idea at its core: a set of rules to edit the pixels
# on the screen. At each iteration, run all the pixels through the rules,
# then we will have an updated pixels, and then continue iterating.
# This will appear as if the thing on the screen (consists of pixels) is 
# moving and transforming and changing.
# This probably isn't how individual living thing live, but it certainly emits
# that illusion. A fun project indeed.

# Rules
# 1 - any live cell with fewer than two live neighbors dies, as if caused by under-population
# 2 - any live cell with two or three live neighbors lives on to the next generation
# 3 - any live cell with more than three live neighbors dies, as if by over-population
# 4 - any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

# Update Generation
# these four rules are applied to all cells simultaneously
# all cells are updated at the same time from the same initial state

# Code Structure
# - initial state: either randomly generated or let user specify
# - a evolve function: input a matrix that represent the living thing, and
#   calculate how each element should behave according to the set of rules
# - a loop: to interate this evolution process
# - a image generation function: to output the evolved matrix after each 
#   iteration.


# Further, a 3D version of this..


import numpy
import matplotlib.pyplot as plt

class GameOfLife:

    def __init__(self):
        """ initial state """
        self.fig = plt.figure()
        self.ax = self.fig.gca()
        self.fig.show()
        # randomly generate an initial state
        self.population = numpy.random.randint(2, size = (100, 100))
        # [TODO] let user define the initial state
    
    def evolve(self):
        """ use evolution rules to evolute the input map """
        population_buffer = self.population
        i, j = population_buffer.shape
        cells = numpy.array(numpy.meshgrid(range(i), range(j))).T.reshape(-1, 2)
        for coord in cells:
            # coordinate of a cell: n[0], n[1]
            if coord[0] == 0:
                # top row
                if coord[1] == 0:
                    # left most
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] + 1, coord[1]:(coord[1]+2)])
                elif coord[1] == j - 1:
                    # right most
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] - 1] + \
                    sum(population_buffer[coord[0] + 1, (coord[1]-1):(coord[1]+1)])
                else:
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] - 1] + \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] + 1, (coord[1] - 1):(coord[1]+2)])
            elif coord[0] == i - 1:
                # bottom row
                if coord[1] == 0:
                    # left most
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] - 1, coord[1]:(coord[1]+2)])
                elif coord[1] == j - 1:
                    # right most
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] - 1] + \
                    sum(population_buffer[coord[0] - 1, (coord[1]-1):(coord[1]+1)])
                else:
                    neighbor_sum = \
                    population_buffer[coord[0], coord[1] - 1] + \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] - 1, (coord[1] - 1):(coord[1]+2)])
            else:
                if coord[1] == 0:
                    # left most
                    neighbor_sum = \
                    sum(population_buffer[coord[0] - 1, (coord[1]):(coord[1]+2)]) + \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] + 1, (coord[1]):(coord[1]+2)])
                elif coord[1] == j - 1:
                    # right most
                    neighbor_sum = \
                    sum(population_buffer[coord[0] - 1, (coord[1] - 1):(coord[1]+1)]) + \
                    population_buffer[coord[0], coord[1] - 1] + \
                    sum(population_buffer[coord[0] + 1, (coord[1] - 1):(coord[1]+1)])
                else:
                    neighbor_sum = \
                    sum(population_buffer[coord[0] - 1, (coord[1] - 1):(coord[1]+2)]) + \
                    population_buffer[coord[0], coord[1] - 1] + \
                    population_buffer[coord[0], coord[1] + 1] + \
                    sum(population_buffer[coord[0] + 1, (coord[1] - 1):(coord[1]+2)])

            # apply rules now
            if self.population[coord[0], coord[1]] == 1:
                # what happens to live cell
                if neighbor_sum < 2 or neighbor_sum > 3:
                    self.population[coord[0], coord[1]] = 0
                else:
                    self.population[coord[0], coord[1]] = 1
            else:
                # what happens to dead cell
                if neighbor_sum == 3:
                    self.population[coord[0], coord[1]] = 1
                else:
                    self.population[coord[0], coord[1]] = 0


    def play(self):
        # display image
        for i in range(100000):
            plt.cla() # clear axes
            self.ax.axis('off') # hide x, y axes
            self.ax.imshow(self.population, cmap = plt.cm.gray)
            self.fig.canvas.draw()
            self.evolve()
            plt.pause(0.1)


if (__name__ == '__main__'):
    game = GameOfLife()
    game.play()