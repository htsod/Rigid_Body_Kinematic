# force_class.py
# Max Liang
# created 01/03/2023
# Description:
#
#
#
#


import numpy as np


class force:
    def __init__(self, position=np.array([0, 0, 0]), magnitude=np.array([0, 0, 0])):
        self.pos = position
        self.mag = magnitude


class force_field:
    def __init__(self, grid_class):
        self.field = np.zeros(grid_class.N**3)

    def generate_field(self, grid_class, func):
        for index, pos in enumerate(grid_class.grid):
            self.field[index] = force(pos, func(pos))

