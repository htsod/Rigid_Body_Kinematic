# grid.py
# Max Liang
# created 01/01/2023
# Description:
#
#
#
#


import numpy as np


class grid:
    def __init__(self, N, center):
        self.N = N
        self.center = center
        self.grid = np.array([np.array([x, y, z]) for x in range(-N/2-center[0], N/2+center[0]) for y in range(-N/2-center[1], N/2+center[1]) for z in range(-N/2-center[2], N/2+center[2])])
        self.vals = np.zeros(N**3)
        self.obj_count = 0

    def empty_grid(self):
        N = self.N
        center = self.center
        emp_grid = np.array([(x, y, z) for x in range(-N / 2 - center[0], N / 2 + center[0]) for y in
                  range(-N / 2 - center[1], N / 2 + center[1]) for z in range(-N / 2 - center[2], N / 2 + center[2])])
        return emp_grid

    def empty_vals(self):
        return np.zeros(self.N**3)



