# Conway's game of life
# This thing has a simple idea at its core: a set of rules to edit the pixels
# on the screen. At each iteration, run all the pixels through the rules,
# then we will have an updated pixels, and then continue iterating.
# This will appear as if the thing on the screen (consists of pixels) is 
# moving and transforming and changing.
# This probably isn't how individual living thing live, but it certainly emits
# that illusion. A fun project indeed.


# Structure
# - initial state: either randomly generated or let user specify
# - a evolve function: input a matrix that represent the living thing, and
#   calculate how each element should behave according to the set of rules
# - a loop: to interate this evolution process
# - a image generation function: to output the evolved matrix after each 
#   iteration.


import numpy
import pil
import random

class GameOfLife:

    def __init__(self):
        """ initial state """
        
        